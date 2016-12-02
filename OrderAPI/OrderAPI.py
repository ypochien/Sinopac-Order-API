class OrderAPI(object):
    def __init__(self, config_file=None):
        self.config_file = config_file

    @property
    def status(self):
        return '已登入'
