# coding: utf-8
#/*##########################################################################
# Copyright (C) 2017 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
#############################################################################*/

"""
This module is used to manage the rsync between files for transfert.
"""

__authors__ = ["H.Payno"]
__license__ = "MIT"
__date__ = "11/04/2017"

from tomwer.core.utils.Singleton import singleton
from tomwer.web.client import OWClient
import subprocess
import functools
import shutil
import time
import sys
import os
from silx.gui import qt
from queue import Queue
from tomwer.core.log import TomwerLogger

logger = TomwerLogger(__name__)


@singleton
class RSyncManager(OWClient, qt.QObject):
    """The manager is managing stacks to call the `rsync` command of the
    system.
    This is used to make interface and make sure only command to rsync is
    called for a tuple of (source folder, target folder) and avoid overhead.
    """

    def __init__(self):
        qt.QObject.__init__(self)
        OWClient.__init__(self, logger)
        self.rsyncQueues = {}
        """link couple of (source, target) to a Queue of thread. Because rsync
        action can't be runned in concurence."""
        self.rmfiles = {}
        self._forceSync = False

    def setForceSync(self, b):
        """
        will wait every time to the worker until the operation is not done
        """
        if b is True:
            logger.info('RSyncManager synchronisation forced')
        else:
            logger.info('RSyncManager synchronisation release')

        self._forceSync = b

    def syncBlissSequence(self, source_scans, target_scans, proposal_file,
                          target_proposal_file, sample_file, target_sample_file,
                          nx_file, target_nx_file, block, delete, callback,
                          callback_parameters, setAllRights=False,
                          parallel=False, verbose=False):
        options = ['--recursive', '--times']
        if delete is True:
            options.append('--remove-source-files')
        else:
            options.append('--update')

        if verbose is True:
            options.append('--verbose')

        if setAllRights is True:
            options.append('--perms --chmod=777')

        return self._syncBlissRawRaw(source_scans=source_scans,
                                     target_scans=target_scans,
                                     proposal_file=proposal_file,
                                     target_proposal_file=target_proposal_file,
                                     sample_file=sample_file,
                                     target_sample_file=target_sample_file,
                                     nx_file=nx_file,
                                     target_nx_file=target_nx_file,
                                     block=block,
                                     callback=callback,
                                     callback_parameters=callback_parameters,
                                     parallel=parallel)

    def syncFolder(self, source, target, block=False, delete=False,
                   callback=None, callback_parameters=None, parallel=False,
                   verbose=False, setAllRights=False):
        """sync a folder

        :param str source: the path of the folder to sync
        :param str target:
        :param bool block: Standard behavior is to create a thread dealing with
                           rsync hen release RSyncManager. If block is True
                           then RSync will wait until the thread is processed.
        :param bool delete: if True, will delete the source folder after sync
        :param callback: function to launch once the thread is terminated
        :param callback_parameters: parameters to give to hte callback
        :param bool parallel: True if we want to launch rsync in parallel mode.
        :param bool verbose: True if we want to call Rsync in verbose mode
        :param bool setAllRights: True if we want to run a chmod 777 on
                                  transfered files
        """
        options = ['--recursive', '--times']
        if delete is True:
            options.append('--remove-source-files')
        else:
            options.append('--update')

        if verbose is True:
            options.append('--verbose')

        if setAllRights is True:
            options.append('--perms --chmod=777')

        return self.syncFolderRaw(source=source,
                                  target=target,
                                  options=options,
                                  block=block,
                                  callback=callback,
                                  callback_parameters=callback_parameters,
                                  parallel=parallel)

    def _getQueue(self, key, finishHandler):
        if key not in self.rsyncQueues:
            rsyncQueue = _RSyncQueue()
            rsyncQueue.sigQueueFinished.connect(finishHandler)
            self.rsyncQueues[key] = rsyncQueue
        return self.rsyncQueues[key]

    def removeDir(self, dir, block=False):
        """
        Remove the scan source when all synchronisation on it are finished

        :param dir: the directory to remove
        """
        _queue = self._getQueue((dir, None), self._managedFinishedRm)
        _queue.addAction(action='rmdir',
                         source=dir)
        if block is True or self._forceSync is True:
            self.rsyncQueues[(dir, None)].rsyncThread.wait()

    def hasActiveSync(self, source, target, timeout=6)-> bool:
        """
        Check if a synchronization between source and target exists

        :param str source:
        :param str target:
        :return:
        :rtype: bool
        """
        command = ' '.join(['ps -aux', '| grep rsync', '|grep ' + source,
                            '|grep ' + target, '| wc -l'])
        with subprocess.Popen(command, shell=True, stdout=subprocess.PIPE) as process:
            try:
                stdout, stderr = process.communicate(input=None,
                                                     timeout=timeout)
            except subprocess.TimeoutExpired:
                process.kill()
                logger.error('timeout exceeded')
                raise subprocess.TimeoutExpired(process.args, timeout,
                                                output=stdout,
                                                stderr=stderr)
            except:  # Including KeyboardInterrupt, communicate handled that.
                process.kill()
                # We don't call process.wait() as .__exit__ does that for us.
                raise
            else:
                try:
                    out = stdout.decode('utf-8')
                except:
                    logger.error('Fail to decode stdout')
                    return False
                else:
                    try:
                        n_rsync = int(out) - 1
                    except Exception as e:
                        logger.error('fail to convert (return of the command '
                                     'should be an int)', str(e))
                        return False
                    else:
                        return n_rsync > 1

    def removeSyncFiles(self, dir, files, block=False):
        """
        Remove some files from a specific forlder but taking into account the
        fact some files could have been synchronized or under synchronization.

        :param dir: origin of the directory
        :param files: files to remove
        :param bool block: Standard behavior is to create a thread dealing with
        """
        _filesToRemove = set(files)
        # take into account ongoing sync
        if dir in self.rsyncQueues:
            for f in files:
                _filesToRemove.add(f.replace(dir, self.rsyncQueues[dir]))

        _queue = self._getQueue((dir, None), self._managedFinishedRm)
        _queue.addAction(action='rm',
                         source=dir,
                         files=_filesToRemove)
        if block is True or self._forceSync is True:
            self.rsyncQueues[(dir, None)].rsyncThread.wait()

    def syncFolderRaw(self, source, target, options, block=False,
                      callback=None, callback_parameters=None, parallel=False):
        """sync a folder launching directly the options given. Used for
        benchmarking.

        :param str source: the path of the folder to sync
        :param str target:
        :param bool block: Standard behavior is to create a thread dealing with
            rsync hen release RSyncManager. If block is True then RSync will
            wait until the thread is processed.
        :param list options: the list of options to apply
        :param handler: function to launch once the thread is terminated
        :param bool parallel: True if we want to launch rsync in parallel mode.
        """
        target = target.rstrip(os.path.sep)
        if not os.path.isdir(target):
            try:
                os.makedirs(target)
            except Exception as e:
                err = 'Unable to create target dir {}. Error is {}'.format((target, str(e)))
                return
        if block is True or self._forceSync is True:
            # wait until al thread are ended
            while (source, target) in self.rsyncQueues:
                self.rsyncQueues[(source, target)].wait()

        _queue = self._getQueue((source, target), self._managedFinishedSync)
        _queue.add(source=source, target=target, options=options,
                   parallel=parallel, callback=callback,
                   callback_parameters=callback_parameters)

        if block is True or self._forceSync is True:
            self.rsyncQueues[(source, target)].rsyncThread.wait()

    def _managedFinishedSync(self, source, target):
        if self.rsyncQueues[(source, target)].empty() is True:
            self.rsyncQueues[(source, target)].sigQueueFinished.disconnect(
                self._managedFinishedSync)
            del self.rsyncQueues[(source, target)]

    def _managedFinishedRm(self, source):
        if self.rsyncQueues[(source, None)].empty() is True:
            self.rsyncQueues[(source, None)].sigQueueFinished.disconnect(
                self._managedFinishedRm)
            del self.rsyncQueues[(source, None)]

    @staticmethod
    def canUseRSync():
        if not sys.platform.startswith('linux'):
            return False
        try:
            subprocess.call(["rsync", "--version"], stdout=subprocess.PIPE)
        except OSError:
            return False
        else:
            return True

    @staticmethod
    def getRSyncCommand(source, target, options, parallel):
        command = ""
        if parallel is True and RSyncManager().canUseParallel():
            command += "parallel -j8 "
        command = "rsync"
        for option in options:
            command += " " + option
        command += " " + source
        command += " " + target
        return command

    @staticmethod
    def canUseParallel():
        """True if we can use rsync in parallel mode"""
        try:
            subprocess.call(["parallel", "--version"], stdout=subprocess.PIPE)
        except OSError:
            return False
        else:
            return True

    @staticmethod
    def syncFile(src, dst):
        """synchronize the two files inplace.
        warning: won't create any stack for it"""
        try:
            subprocess.call(["rsync", src, dst, '--inplace'])
        except OSError as e:
            logger.error('fail to symchronize files', src, dst, '. Reason is', e)


class SetQueue(Queue):
    """Queue with a set behavior. In the sense that a requested thread
    synchronization could not be present twice"""
    def __init__(self, maxsize=0):
        Queue.__init__(self, maxsize)
        self._existing = []

    def put(self, val):
        thread, callbacks = val
        _id = self._getID(thread)
        if _id in self._existing:
            return
        else:
            self._existing.append(_id)
            Queue.put(self, val)

    def get(self):
        thread, callbacks = Queue.get(self)
        _id = self._getID(thread)
        if _id in self._existing:
            self._existing.remove(_id)
        return thread, callbacks

    def _getID(self, thread):
        """
        Get hash from thread source, target and options / files to make sure
        actions are uniques and won't be stored several time
        """
        if isinstance(thread, _RmThread):
            return (thread.source, None, thread.files)
        elif isinstance(thread, _RSyncThread):
            return (thread._source, thread._target, thread._options)
        elif isinstance(thread, _RmDirThread):
            return (thread.dir, None)
        else:
            raise ValueError('Unrecognized thread type')


class _RSyncQueue(SetQueue, qt.QObject):
    """
    class to deal with the RSync thread and avoid competition of rsync commands
    """

    sigQueueFinished = qt.Signal(str, str)

    def __init__(self):
        SetQueue.__init__(self)
        qt.QObject.__init__(self)
        self.rsyncThread = None
        self.callback = None
        self.callback_parameters = None
        self.threads = []

    def add(self, source, target, options, parallel, callback, callback_parameters):
        thread = _RSyncThread(source=source,
                              target=target,
                              options=options,
                              parallel=parallel)
        self.threads.append(thread)
        callback_finisher = functools.partial(self.syncFinisher, source, target)
        if callback is not None:
            assert callback_parameters is not None
            handler_callback = functools.partial(callback, *callback_parameters)
            self.put((thread, (callback_finisher, handler_callback)))
        else:
            self.put((thread, (callback_finisher, )))
        if self.canExecNext():
            self.execNext()

    def addAction(self, source, action, files=None):
        assert action in ('rm', 'rmdir')
        if action == 'rm':
            thread = _RmThread(source=source, files=files)
            callback = functools.partial(self.syncFinisher, source, None)
        else:
            thread = _RmDirThread(dir=source)
            callback = functools.partial(self.syncFinisher, source, None)

        self.put((thread, (callback, )))
        if self.canExecNext():
            self.execNext()

    def execNext(self):
        """Launch the next reconstruction if any
        """
        if self.empty():
            return
        assert(self.rsyncThread is None or not self.rsyncThread.isRunning())
        self.rsyncThread, callbacks = self.get()
        for callback in callbacks:
            self.rsyncThread.finished.connect(callback)
        self.rsyncThread.start()

    def canExecNext(self):
        """
        Can we launch an ftserie reconstruction.
        Reconstruction can't be runned in parallel

        :return: True if no reconstruction is actually running
        """
        return self.rsyncThread is None or not self.rsyncThread.isRunning()

    def syncFinisher(self, source, target):
        del self.rsyncThread
        self.rsyncThread = None
        self.callback = None
        self.sigQueueFinished.emit(source, target)
        self.execNext()


class _RSyncThread(OWClient, qt.QThread):
    """Thread dealing with synchronisation
    """

    def __init__(self, source, target, options, parallel):
        qt.QThread.__init__(self)
        OWClient.__init__(self, logger)
        self._source = source
        self._target = target
        self._options = options
        self._parallel = parallel

    def run(self):
        if not os.path.exists(self._source) or not os.path.isdir(self._source):
            logger.info('source folder %s not existing (or no more?)' % self._source)
            return
        if not os.path.exists(self._target) or not os.path.isdir(self._target):
            logger.info('target folder %s not existing (or no more?)' % self._target)
            return
        command = RSyncManager().getRSyncCommand(
            source=self._source,
            target=self._target,
            options=self._options,
            parallel=self._parallel)
        subprocess.call(command, shell=True, stdout=subprocess.PIPE)

        # if delete action have been requested:
        if '--remove-source-files' in self._options:
            if _RSyncThread.removeEmptyFolders(self._source) is False:
                mess = 'fail to remove file on %s.' % self._source
                mess += 'Synchronisation might have failed'
                logger.error(mess)

    @staticmethod
    def removeEmptyFolders(folder):
        if not(os.path.isdir(folder) and os.path.exists(folder)):
            return True

        assert(os.path.isdir(folder))
        subFiles = os.listdir(folder)

        if len(subFiles) == 0:
            os.rmdir(folder)
        else:
            for subFile in subFiles:
                subFolder = os.path.join(folder, subFile)
                if os.path.isdir(subFolder):
                    if not _RSyncThread.removeEmptyFolders(subFolder):
                        return False
                else:
                    return False

            os.rmdir(folder)
        return True


class _RmThread(OWClient, qt.QThread):
    """
    Used to remove a set of files if existing
    """
    def __init__(self, source, files):
        OWClient.__init__(self, logger)
        qt.QThread.__init__(self)
        self.source = source
        self.files = files

    def run(self):
        for f in self.files:
            if os.path.isfile(f) and os.path.exists(f):
                os.remove(f)


class _RmDirThread(OWClient, qt.QThread):
    """
    Used to remove a set of files if existing
    """
    def __init__(self, dir):
        OWClient.__init__(self, logger)
        qt.QThread.__init__(self)
        self.dir = dir

    def run(self):
        if os.path.exists(self.dir):
            try:
                shutil.rmtree(self.dir)
            except:
                pass


class RSyncWorker(qt.QThread):
    """Thread which call for a synchronization on a folder each n seconds"""
    def __init__(self, src_dir, dst_dir, delta_time):
        qt.QThread.__init__(self)
        self._src_dir = src_dir
        self._dst_dir = dst_dir
        self._delta_tile = delta_time
        self._stop = False

    def stop(self):
        self._stop = True

    def _process_sync(self):
        RSyncManager().syncFolder(source=self._src_dir,
                                  target=self._dst_dir,
                                  delete=False)
        time.sleep(self._delta_tile)

    def run(self):
        while not self._stop:
            self._process_sync()


class BlissSequenceRSyncWorker(RSyncWorker):
    """Thread to synchronize a bliss sequence"""
    def __init__(self, src_dir, dst_dir, src_proposal_file,
                 dst_proposal_file, delta_time):
        super(BlissSequenceRSyncWorker, self).__init__(src_dir=src_dir,
                                                       dst_dir=dst_dir,
                                                       delta_time=delta_time)
        self._bliss_master_file = src_proposal_file
        self._dst_bliss_master_file = dst_proposal_file

    def _process_sync(self):
        super(BlissSequenceRSyncWorker, self)._process_sync()
        if self._bliss_master_file is not None:
            RSyncManager().syncFile(src=self._bliss_master_file,
                                    dst=self._dst_bliss_master_file)


class BlissSequenceRSyncWorkerFinalizer(qt.QThread):
    def __init__(self, source_scans, target_scans, proposal_file,
                 target_proposal_file, sample_file, target_sample_file,
                 nx_file, target_nx_file, block, callback, callback_parameters,
                 parallel, delta_time=0.5):
        self._sources_scans = source_scans
        self._target_scans = target_scans
        self._proposal_file = proposal_file
        self._target_proposal_file = target_proposal_file
        self._sample_file = sample_file
        self._target_sample_file = target_sample_file
        self._nx_file = nx_file
        self._target_nx_file = target_nx_file
        self._block = block
        self._callback = callback
        self._callback_parameters = callback_parameters
        self._parparallel = parallel

        self._n_callback_scans = 0
        self._n_callback_proposal = 0
        self._n_callback_sample = 0
        self._delta_time = delta_time

    def scan_transfert_completed(self):
        return self._n_callback_scans == len(self._sources_scans)

    def proposal_file_completed(self):
        return True
        if self._proposal_file is None:
            return True
        else:
            return self._n_callback_proposal == 1

    def sample_file_completed(self):
        return True
        if self._sample_file is None:
            return True
        else:
            return self._n_callback_sample == 1

    def transfert_completed(self):
        return self.proposal_file_completed() and self.sample_file_completed() and self.scan_transfert_completed()

    def _callback_scans(self, *args, **kwargs):
        self._n_callback_scans = self._n_callback_scans + 1

    def _callaback_sample_file(self, *args, **kwargs):
        self._n_callback_sample = 1

    def _callback_proposal_file(self, *args, **kwargs):
        self._n_callback_proposal = 1

    def run(self):
        # no callback
        if self._sample_file is not None:
            RSyncManager().syncFile(src=self._sample_file,
                                    dst=self._target_sample_file)

        if self._proposal_file is not None:
            RSyncManager().syncFile(src=self._proposal_file,
                                    dst=self._target_proposal_file)

        for scan_in, scan_out in zip(self._sources_scans, self._target_scans):
            RSyncManager().syncFolder(source=scan_in,
                                      target=scan_out,
                                      callback=self._callback_scans,
                                      delete=True)

        while not self.transfert_completed():
            time.sleep(self._delta_time)

        if self._callback:
            if self._callback_parameters is not None:
                self._callback(*self._callback_parameters)
            else:
                self._callback()
