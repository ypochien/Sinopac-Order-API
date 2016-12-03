import json

from OrderAPI.pyT4 import pyT4


class OrderAPI(object):
    def __init__(self, config_file=None):
        with open(config_file) as fd_json:
            self.UserInfo = json.load(fd_json)

        msg = pyT4.init_t4(self.UserInfo['UserId'].encode('utf-8'), self.UserInfo['Password'].encode('utf-8'),
                           ''.encode('utf-8'))
        new_msg = str(msg, 'cp950')
        self._status = new_msg
        pyT4.do_register(1)

    @property
    def status(self):
        return self._status

    @property
    def server_ip(self):
        return str(pyT4.show_ip(), 'cp950')

    @status.setter
    def status(self, value):
        self._status = value
