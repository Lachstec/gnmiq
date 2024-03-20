import tomllib

class Configuration:
    '''
    Contains configuration values for the application.
    The values are as follows:
        targets: List of URLs to gNMI capable network devices to monitor (required)
        username: Used to authenticate to the network devices (required)
        password: Used to authenticate to the network devices (required)
        mq_url: URL to the message queue where changes in configuration should be submitted (required)
        paths: gNMI paths that should be subscribed to
    '''
    def __init__(self):
        self.targets: list[str] = []
        self.username: str = ''
        self.password: str = ''
        self.mq_url: str = ''
        self.paths: list[str] = []

    '''
    Read the configuration file located at specified path.
    Raises an Exception if a required value is not supplied or if the config file is not valid TOML.
    '''
    def read_file(self, path: str):
        with open(path, 'rb') as conf_file:
            config = tomllib.load(conf_file)
            values = config['gnmiq']
            self.targets = values['targets']
            self.username = values['username']
            self.password = values['password']
            self.mq_url = values['mq_url']
            self.paths = values['paths']

