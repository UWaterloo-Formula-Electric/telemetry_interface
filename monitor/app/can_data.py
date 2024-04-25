
from typing import Any
import cantools

class DBC:
    def __init__(self, path: str):
        self.path = path
        self.dbc = self._load_dbc()
        self.lookup = self._create_lookup()
        self.cantools_db = cantools.database.load_file(path)

    def get_dbc_data(self, signal: str):
        return self.lookup[signal]
    
    def _load_dbc(self):
        import canmatrix.formats
        dbc = canmatrix.formats.loadp_flat(self.path)
        return dbc

    def _create_lookup(self):
        lookup = {}
        for message in self.dbc:
            for signal in message.signals:
                signal_info = {
                    "msg_id": message.arbitration_id.id,
                    "msg_name": message.name,
                    "is_dtc": is_dtc(message.arbitration_id.id),
                    "sender": message.transmitters,
                    "receivers": message.receivers,
                }
                lookup[signal.name] = signal_info
        return lookup

class Signal:
    def __init__(self, signal_name: str, value: Any, timestamp: float, dbc: DBC):
        self.signal_name = signal_name
        self.value = value
        self.timestamp = timestamp

        self.dbc = dbc

        self.msg_name = dbc.get_dbc_data(signal_name)["msg_name"]
        self.msg_id = dbc.get_dbc_data(signal_name)["msg_id"]
        self.is_dtc = dbc.get_dbc_data(signal_name)["is_dtc"]
        self.sender = dbc.get_dbc_data(signal_name)["sender"]
        self.receivers = dbc.get_dbc_data(signal_name)["receivers"]

    def __str__(self):
        return f"{self.timestamp:.6f}, [{self.msg_name}] {self.signal_name}, {self.value} - from {self.sender} to {self.receivers}"

    def __repr__(self):
        return str(self)


def is_dtc(id: int) -> bool:        
    priority_mask = 0b111 << 26
    is_dtc = (id & priority_mask) == 0
    return is_dtc