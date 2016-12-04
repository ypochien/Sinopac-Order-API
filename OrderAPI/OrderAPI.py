import json

from OrderAPI.pyT4.pyT4 import T4

ACCOUNT_TYPE = {
    'S': '股票',
    'F': '期貨'
}


class User(object):
    def __init__(self, acc):
        """
        S9A95 - 9809315 - 楊伯謙
        FF002000 - 9114728 - 楊伯謙
        """
        self.type = acc.split('-')[0].strip()[0]
        self.branch = acc.split('-')[0].strip()[1:]
        self.account = acc.split('-')[1].strip()
        self.name = acc.split('-')[2].strip()

    def __str__(self):
        return '{}-{}{}-{}'.format(ACCOUNT_TYPE[self.type], self.branch, self.account, self.name)


class OrderAPI(object):
    @classmethod
    def accounts(cls):
        accounts = T4.show_list2()
        accounts = [acc for acc in accounts.split('\n') if len(acc)]
        for acc in accounts:
            yield User(acc)

    def __init__(self, config_file='OrderAPI.json'):
        self._init_t4(config_file)
        self.accounts = [acc for acc in OrderAPI.accounts()]

    def _init_t4(self, config_file):
        with open(config_file) as fd_json:
            self.UserInfo = json.load(fd_json)
        msg = T4.init_t4(self.UserInfo['UserId'], self.UserInfo['Password'], '')
        self._status = msg
        T4.do_register(1)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self.status = value

    @property
    def server_ip(self):
        ip_port = T4.show_ip()
        ip = ip_port.split('\n')[0].split(':')[1].strip()
        port = ip_port.split('\n')[1].split(':')[1].strip()
        return '{}:{}'.format(ip, port)

    def get_account_list(self):
        return self.accounts
