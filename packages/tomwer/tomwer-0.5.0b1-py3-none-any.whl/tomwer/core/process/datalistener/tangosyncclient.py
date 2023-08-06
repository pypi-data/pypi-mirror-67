from bliss.data.node import get_session_node
from bliss.data.events import EventType
# note: if you install bliss with --no-deps option you should remove the import of
# from bliss.common.tango import DevFailed, DevState in bliss.common.logtools.py
import time
import logging
import threading
import typing
from silx.utils.enum import Enum as _Enum

# logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)


class TangoAcquisitionStatus(_Enum):
    """list of possible status of the acquisition"""
    STARTED = 'started'
    ON_GOING = 'on going'
    CANCELED = 'canceled'
    ENDED = 'ended'


class _TangoState:
    MOVING = 'moving'
    ON = 'on'
    FAULT = 'fault'


class TangoAcquisition:
    """Define an acquisition made with tango / tango"""

    def __init__(self, file_path, entry_name, proposal_file, start_time):
        self.entry = entry_name
        self.master_file = file_path
        self.proposal_file = proposal_file
        self.scan_numbers = []
        self.status = TangoAcquisition
        self._start_time = start_time
        self._end_time = None
        self._error = None
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    def add_scan_number(self, scan_number):
        self.scan_numbers.append(scan_number)

    def set_status(self, status):
        self.status = TangoAcquisitionStatus.from_value(status)

    def end(self, end_time, succeed: bool, error: typing.Union[None, str]):
        if succeed is True:
            self.status = TangoAcquisitionStatus.ENDED
        else:
            self.status = TangoAcquisitionStatus.CANCELED
        self._error = error
        self._end_time = end_time

    @property
    def has_error(self):
        return self._error is not None

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time

    @property
    def error(self) -> typing.Union[None, str]:
        return self.error


class _BaseDataListenerThread:
    """Base class for data listener thread. Thread can be a threading.Thread
    or a qt.QThread.

    On the current bliss system (2020) a sequence is an acquisition. A sequence
    is composed of several scans. A scan can be the 'init' information,
    dark frames, flat frames, projections frames, return projections...

    :param str device_name: name of the tango device proxy
    :param Union[None, list]: list of the tango acquisitions
    """

    def __init__(self, device_name: str, acquisitions=None,
                 only_new_events=True):
        # connect to the tango device
        self._device_name = device_name
        # self.device = self.get_device(device_name=self._device_name)  # tango.DeviceProxy(_TANGO_DEVICE_NAME)
        self.acquisitions = acquisitions or []
        """acquisition with scan information, as key and acquisition status
        as value"""
        self._stop = False
        self._tomo_state = None
        # state of the current sequence
        self._current_sequence = None
        # current sequence
        self._current_scan_number = None
        # scan of the sequence currently recording
        self._only_new_events = only_new_events

    @property
    def session(self):
        return self._device_name

    def stop(self) -> None:
        """
        ask the thread to stop
        """
        self._stop = True

    def sequence_started(self, acquisition: TangoAcquisition) -> None:
        """
        function called when an acquisition is started

        :param acquisition: acquisition started
        """
        print('++ new sequence added')

    def new_scan_added(self, acquisition: TangoAcquisition,
                       scan_number: int) -> None:
        """
        function called when a new scan is added to an acquisition

        :param acquisition: acquisition on going
        :param scan_number: number of the scan added
        :return:
        """
        print('new scan added')

    def sequence_ended(self, acquisition: TangoAcquisition) -> None:
        """
        function called when a new scan is ended

        :param acquisition: acquisition ended
        """
        print('-- sequence ended')

    def get_sequence_scan_number(self, node):
        return node.info['technique']['scan']['sequence']

    def get_saving_file(self, node):
        return node.info['filename']

    def get_scan_number(self, node):
        return node.info['scan_nb']

    def get_scan_title(self, node):
        return node.info['technique']['scan']['sequence']
    
    def get_entry_name(self, node):
        return '.'.join((str(node.info['scan_nb']), str(1)))

    def get_proposal_file(self, node):
        return node.info['nexuswriter']['masterfiles']['proposal']

    def _new_sequence_discovered(self, node):
        self._current_acquisition = TangoAcquisition(
            file_path=self.get_saving_file(node=node),
            entry_name=self.get_entry_name(node=node),
            proposal_file=self.get_proposal_file(node=node),
            start_time=time.ctime())
        self.acquisitions.append(self._current_acquisition)
        self.sequence_started(self._current_acquisition)
        self._current_acquisition.state = _TangoState.MOVING

    def run(self) -> None:

        _logger.info('connect to bliss with: {}'.format(self._device_name))

        # waiting for a sequence to start
        while not self._stop:
            self._current_acquisition = None
            try:
                session_node = get_session_node(self.session)
                filter_ = ['scan_group', 'scan']
                # try:
                if self._only_new_events is True:
                    session_it = session_node.iterator.walk_on_new_events(
                        filter=filter_)
                else:
                    session_it = session_node.iterator.walk(filter=filter_)

                for event_type, node, event_data in session_it:
                    if event_type == EventType.NEW_NODE and node.type == 'scan_group':
                        try:
                            self._new_sequence_discovered(node=node)
                        except Exception as e:
                            _logger.error(e)

                    # get information on the running tomo scans
                    if not self._stop and self._current_acquisition and self._current_acquisition.state == _TangoState.MOVING:
                        # started scan in the sequence
                        if event_type == EventType.NEW_NODE and node.type == 'scan':
                            self._current_scan_number = self.get_scan_number(
                                node=node)
                            _logger.info(
                                'One scan from the sequence is started: {}'.format(
                                    self._current_scan_number))

                        # ended scan in the sequence
                        if event_type == EventType.END_SCAN and node.type == 'scan':
                            _logger.info(
                                'One scan from the sequence is ended: {}'.format(
                                    self._current_scan_number))
                            self._current_acquisition.add_scan_number(
                                self._current_scan_number)
                            self._current_acquisition.set_status(
                                TangoAcquisitionStatus.ON_GOING)
                        # ended tomo sequence
                        if event_type == EventType.END_SCAN and node.type == 'scan_group':
                            self._current_acquisition.state = _TangoState.ON
                            self._current_acquisition.end(
                                end_time=time.ctime(),
                                succeed=True,
                                error=None)
                            self.sequence_ended(
                                acquisition=self._current_acquisition)
                            break

                    if self._stop:
                        return

            except Exception as e:
                _logger.error(e)
                if self._current_acquisition is not None:
                    self._current_acquisition.state = _TangoState.FAULT
                    self._current_acquisition.end(end_time=time.ctime(),
                                                  succeed=False,
                                                  error=str(e))
                    self.sequence_ended(acquisition=self._current_acquisition)


class DataListenerThread(_BaseDataListenerThread, threading.Thread):
    """Implementation of _BaseDataListenerThread with a threading.Thread"""

    def __init__(self, device, acquisitions=None):
        threading.Thread.__init__(self)
        _BaseDataListenerThread.__init__(self, device=device,
                                         acquisitions=acquisitions)


if __name__ == '__main__':
    session = 'HRTOMO'
    worker = _BaseDataListenerThread(device_name=session, only_new_events=True)
    worker.run()
    exit(0)
