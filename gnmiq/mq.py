import pika

class MQClient:
    def __init__(self, host: str):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = connection.channel()
        self.channel.queue_declare('gnmi_changes')

    def publish_change(self, change):
        self.channel.basic_publish(exchange='', routing_key='gnmi_changes', body=change)
        