from pygnmi.client import gNMIclient

class GNMICollector:
    def __init__(self, targets: list[str]):
        self.targets = targets

    