import pika

class MQClient:
    def __init__(self, host: str, targets: list[str]):
        self.targets = targets
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = connection.channel()
        for target in targets:
            self.channel.queue_declare('gnmi_changes-{}'.format(target))

    def publish_change(self, target: str, change):
        self.channel.basic_publish(exchange='', routing_key='gnmi_changes-{}'.format(target), body=change)
        