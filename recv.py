import pika
import sys
import os

def callback(ch, method, properties, body):
    print(f" [X] Received: {body}")

def main():
    conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = conn.channel()
    channel.basic_consume(queue='gnmi_changes-clab-srl01-srl', auto_ack=True, on_message_callback=callback)
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
