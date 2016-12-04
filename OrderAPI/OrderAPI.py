import json
import struct
from collections import namedtuple

from OrderAPI.pyT4.pyT4 import T4

ACCOUNT_TYPE = {
    'S': '股票',
    'F': '期貨',
    'H': '港股'
}


class Account(object):
    def __init__(self, acc):
        """
        S9A95 - 9809315 - 楊伯謙
        FF002000 - 9114728 - 楊伯謙
        """
        self.type = acc.split('-')[0].strip()[0]
        self.branch = acc.split('-')[0].strip()[1:]
        self.account = acc.split('-')[1].strip()
        self.name = acc.split('-')[2].strip()


class OrderAPI(object):
    @staticmethod
    def make_stock_orders(stock, qty, price):
        res = {
            'stock': stock,
            'price': str(price),
            'price_type': ' '
        }
        if qty > 0:
            bs = 'B'
        else:
            bs = 'S'
        res['bs'] = bs
        res['qty'] = str(abs(qty))
        res['ord_type'] = '00'
        return res

    @staticmethod
    def accounts():
        accounts = T4.show_list2()
        accounts = [acc for acc in accounts.split('\n') if len(acc)]
        for acc in accounts:
            yield Account(acc)

    def __init__(self, config_file='OrderAPI.json'):
        self._init_t4(config_file)
        self._init_ca()

    def _init_ca(self):
        self.accounts = {'S': [], 'F': [], 'H': []}
        for acc in OrderAPI.accounts():
            for ekey in self.UserInfo['CA']:
                T4.add_acc_ca(acc.branch, acc.account, ekey['ID'], ekey['eKey'], ekey['eKeyPassword'])
            self.accounts[acc.type].append(acc)

    def _init_t4(self, config_file):
        with open(config_file) as fd_json:
            self.UserInfo = json.load(fd_json)
        msg = T4.init_t4(self.UserInfo['UserId'], self.UserInfo['Password'], '')
        self._status = msg
        T4.do_register(1)

    @property
    def status(self):
        return self._status

    @property
    def server_ip(self):
        ip_port = T4.show_ip()
        ip = ip_port.split('\n')[0].split(':')[1].strip()
        port = ip_port.split('\n')[1].split(':')[1].strip()
        return '{}:{}'.format(ip, port)

    @staticmethod
    def placing_order(acc, dt_orders):
        order_args = list()
        order_args.append(dt_orders['bs'])
        order_args.append(acc.branch)
        order_args.append(acc.account)
        order_args.append(dt_orders['stock'])
        order_args.append(dt_orders['ord_type'])
        order_args.append(dt_orders['price'])
        order_args.append(dt_orders['qty'])
        order_args.append(dt_orders['price_type'])
        return T4.stock_order(*order_args)

    @staticmethod
    def placing_cancel_order(dt_cancel):
        lst_cancel_items = list()
        lst_cancel_items.append(dt_cancel['bs'])
        lst_cancel_items.append(dt_cancel['branch'])
        lst_cancel_items.append(dt_cancel['account'])
        lst_cancel_items.append(dt_cancel['stock'])
        lst_cancel_items.append(dt_cancel['ord_type'])
        lst_cancel_items.append(dt_cancel['ord_seq'])
        lst_cancel_items.append(dt_cancel['ord_no'])
        lst_cancel_items.append(dt_cancel['pre_order'])
        return T4.stock_cancel(*lst_cancel_items)
