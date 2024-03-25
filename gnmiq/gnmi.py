from pygnmi.client import gNMIclient
from gnmiq.mq import MQClient
from gnmiq.config import Configuration
import json

class GNMICollector:
    '''
    Subscribes to all paths on all targets specified in `config` and submits them to a RabbitMQ.
    '''
    def __init__(self, config: Configuration, mq_client: MQClient):
        self.config = config
        self.mq = mq_client

    def monitor(self):
        req = {
            'subscription': []
        }
        for path in self.config.paths:
            path_request = {
                'path': path,
                'mode': 'on_change',
                'updates_only': True,
            }
            req['subscription'].append(path_request)
        for target in self.config.targets:
            with gNMIclient(target=(target, '57400'), username=self.config.username, password=self.config.password) as gnmi:
                telemetry_stream = gnmi.subscribe_stream(subscribe = req)
                entries = []
                for entry in telemetry_stream:
                    self.mq.publish_change(target, json.dumps(entry))

    