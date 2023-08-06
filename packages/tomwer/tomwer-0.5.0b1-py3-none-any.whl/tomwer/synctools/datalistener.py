# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016 European Synchrotron Radiation Facility
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
# ###########################################################################*/

__authors__ = ["H. Payno"]
__license__ = "MIT"
__date__ = "16/03/2020"


from tomwer.core.process.datalistener.tangosyncclient import _BaseDataListenerThread
from tomwer.core.process.datalistener.tangosyncclient import TangoAcquisition
from tomwer.core.process.datalistener.tangosyncclient import TangoAcquisitionStatus
from collections import namedtuple
from datetime import datetime
from silx.gui import qt
from tomwer.utils import docstring
import time

import logging

_logger = logging.getLogger(__name__)


class DataListenerQThread(_BaseDataListenerThread, qt.QThread):
    """Implementation of the _BaseDataListenerThread with a QThread"""

    sigAcquisitionStarted = qt.Signal(tuple)
    """Signal emitted when an acquisition is started. Tuple is:
    (master_file, master_entry)"""
    sigAcquisitionEnded = qt.Signal(tuple)
    """Signal emitted when an acquisition is ended. Tuple is 
    (master_file, master_entry, succeed)"""
    sigScanAdded = qt.Signal(tuple)
    """Signal emitted when a scan is added to an acquisition. Tuple is
    (master_file, master_entry, scan_entry)"""
    def __init__(self, device, acquisitions):
        qt.QThread.__init__(self)
        _BaseDataListenerThread.__init__(self, device, acquisitions)

    @docstring(_BaseDataListenerThread.sequence_started)
    def sequence_started(self, acquisition: TangoAcquisition) -> None:
        assert isinstance(acquisition, TangoAcquisition)
        self.sigAcquisitionStarted.emit((acquisition.master_file,
                                         acquisition.entry,
                                         acquisition.proposal_file))

    @docstring(_BaseDataListenerThread.new_scan_added)
    def new_scan_added(self, acquisition: TangoAcquisition, scan_number: int) -> None:
        assert isinstance(acquisition, TangoAcquisition)
        self.sigScanAdded.emit((acquisition.master_file,
                                acquisition.entry,
                                acquisition.proposal_file,
                                scan_number))

    @docstring(_BaseDataListenerThread.new_scan_added)
    def sequence_ended(self, acquisition: TangoAcquisition) -> None:
        assert isinstance(acquisition, TangoAcquisition)
        self.sigAcquisitionEnded.emit((acquisition.master_file,
                                       acquisition.entry,
                                       acquisition.proposal_file,
                                       not acquisition.has_error))

    def join(self, timeout=None):
        if timeout is None:
            self.wait()
        else:
            self.wait(timeout)


_mock_acquisition_info = namedtuple("_mock_acquisition_info",
                                    ["master_file", "entry", "scan_numbers",
                                     "waiting_time"])


class MockDataListenerQThread(DataListenerQThread):
    """
    Redeinfe the run and mock an acquisition for CI avoiding to have a
    tango server and tango install.
    """
    def __init__(self, acquisitions: list, mock_acquisitions: list):
        DataListenerQThread.__init__(self, None, acquisitions=acquisitions)
        assert isinstance(mock_acquisitions, (list, tuple))
        for acqui in mock_acquisitions:
            assert type(acqui) is _mock_acquisition_info
        self.mock_acquisitions = mock_acquisitions
        "waiting time between each scan / step of the acquisition"

    def get_device(self, device_name):
        return None

    def run(self) -> None:
        _logger.info('mock an acquisition using tango / tango')

        for mock_acqui in self.mock_acquisitions:
            if self._stop:
                return

            # first scan is the definition of the acquisition
            now = datetime.now()
            current_acquisition = TangoAcquisition(file_path=mock_acqui.master_file,
                                                   entry_name=mock_acqui.entry,
                                                   start_time=now.strftime("%H:%M:%S"),
                                                   proposal_file=None)
            self.acquisitions.append(current_acquisition)
            self.sequence_started(current_acquisition)

            time.sleep(mock_acqui.waiting_time)

            # add scan numbers if any
            for scan_number in mock_acqui.scan_numbers:
                current_acquisition.add_scan_number(scan_number)
                current_acquisition.set_status(TangoAcquisitionStatus.ON_GOING)
                self.new_scan_added(acquisition=current_acquisition,
                                    scan_number=scan_number)
                if self._stop:
                    return
                time.sleep(mock_acqui.waiting_time)

            # end acquisition
            now = datetime.now()
            current_acquisition.end(end_time=now.strftime("%H:%M:%S"),
                                    succeed=True,
                                    error=None)
            self.sequence_ended(acquisition=current_acquisition)
            time.sleep(mock_acqui.waiting_time)

        # wait until stop the thread
        while not self._stop:
            time.sleep(0.1)
