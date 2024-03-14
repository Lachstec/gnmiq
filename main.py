import argparse
from tomllib import TOMLDecodeError
from gnmiq.config import Configuration

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
    except TOMLDecodeError:
        print('configuration file is not valid toml')
        return
    except FileNotFoundError:
        print('cant find config file "{}"'.format(args.file))
        return
    
    print(config.mq_url)




if __name__ == '__main__':
    main()