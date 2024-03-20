from pygnmi.client import gNMIclient
from gnmiq.mq import MQClient
from gnmiq.config import Configuration

class GNMICollector:
    def __init__(self, config: Configuration):
        self.config = config

    def monitor(self):
        req = {
            'subscription': []
        }
        for path in self.config.paths:
            path_request = {
                'path': path,
                'mode': 'sample',
                'sample_interval': 10000000000
            }
            req['subscription'].append(path_request)
        for target in self.config.targets:
            with gNMIclient(target=(target, '57400'), username=self.config.username, password=self.config.password) as gnmi:
                telemetry_stream = gnmi.subscribe_stream(subscribe = req)

                for entry in telemetry_stream:
                    print(entry)

    