import argparse
from tomllib import TOMLDecodeError
from gnmiq.config import Configuration
from gnmiq.mq import MQClient
from gnmiq.gnmi import GNMICollector

def cli_args():
    parser = argparse.ArgumentParser(
        description='Monitor and publish configuration changes on gNMI capable network devices to a RabbitMQ'
        )
    parser.add_argument('-c', '--config', dest='file', metavar='config-file', type=str, required=True, help='Configuration File')
    return parser.parse_args()

def main():
    args = cli_args()
    config = Configuration()
    try:
        config.read_file(args.file)
        mq_client = MQClient(config.mq_url)
        collector = GNMICollector(config)
        collector.monitor()
    except TOMLDecodeError:
        print('configuration file is not valid toml')
        return
    except FileNotFoundError:
        print('config file "{}" not found'.format(args.file))
        return
    
    print(config.mq_url)




if __name__ == '__main__':
    main()