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

    def __str__(self):
        return '{}-{}{}-{}'.format(ACCOUNT_TYPE[self.type], self.branch, self.account, self.name)


class OrderAPI(object):
    @classmethod
    def make_stock_orders(cls, stock, qty, price):
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
        res['type'] = '00'
        return res

    @classmethod
    def accounts(cls):
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

    @status.setter
    def status(self, value):
        self.status = value

    @property
    def server_ip(self):
        ip_port = T4.show_ip()
        ip = ip_port.split('\n')[0].split(':')[1].strip()
        port = ip_port.split('\n')[1].split(':')[1].strip()
        return '{}:{}'.format(ip, port)

    def placing_order(self, acc, orders):
        """buy_or_sell: "B"=買, "S"=賣, "F"=先賣
            branch: 證券分公司代號
            account: 證券帳戶
            stock_id: 股票代碼
            ord_type: 交易類別
             "P0"=定盤現股, "P3"=定盤融資, "P4"=定盤融券
             "00"=整股現股, "03"=整股融資, "04"=整股融券
             "20"=零股
            price: 價格 6 位數 (定盤、漲跌停時，此參數忽略不作用，會帶 0.0)
            amount: 張數 3 位數 (零股則為股數)
            price_type: " "=限價, "2"=漲停價, "3"=跌停價
        """
        order_args = []
        order_args.append(orders['bs'])
        order_args.append(acc.branch)
        order_args.append(acc.account)
        order_args.append(orders['stock'])
        order_args.append(orders['type'])
        order_args.append(orders['price'])
        order_args.append(orders['qty'])
        order_args.append(orders['price_type'])
        msg = T4.stock_order(*order_args)
        return msg
