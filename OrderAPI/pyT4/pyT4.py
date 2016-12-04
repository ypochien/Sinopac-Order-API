# coding=utf-8
# __author__ == ypochien at gmail.com
import json
import os
import struct
from collections import namedtuple
from ctypes import *
from ctypes.wintypes import *

t4_dir = os.path.dirname(__file__)
api = windll.LoadLibrary(t4_dir + "/t4.dll")

# API Part i.
init_t4 = api.init_t4
init_t4.restype = c_char_p
init_t4.argtypes = [c_char_p, c_char_p, c_char_p, ]

add_acc_ca = api.add_acc_ca
add_acc_ca.restype = c_char_p
add_acc_ca.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p, c_char_p]

verify_ca_pass = api.verify_ca_pass
verify_ca_pass.restype = c_char_p
verify_ca_pass.argtypes = [c_char_p, c_char_p]

# API Part ii.
stock_order = api.stock_order
stock_order.restype = c_char_p
stock_order.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p]

stock_cancel = api.stock_cancel
stock_cancel.restype = c_char_p
stock_cancel.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p]

future_order = api.future_order
future_order.restype = c_char_p
future_order.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p,
                         c_char_p]

future_cancel = api.future_cancel
future_cancel.restype = c_char_p
future_cancel.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p]

future_change = api.future_change
future_change.restype = c_char_p
future_change.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p]

option_order = api.option_order
option_order.restype = c_char_p
option_order.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p,
                         c_char_p, c_char_p, c_char_p, c_char_p]

option_cancel = api.option_cancel
option_cancel.restype = c_char_p
option_cancel.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p]

ffuture_order = api.ffuture_order
ffuture_order.restype = c_char_p
ffuture_order.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p,
                          c_char_p, c_char_p, c_char_p, c_char_p, c_char_p]

ffuture_cancel = api.ffuture_cancel
ffuture_cancel.restype = c_char_p
ffuture_cancel.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p,
                           c_char_p, c_char_p, c_char_p]

# API part iii.
get_response = api.get_response
get_response.restype = c_char_p
get_response.argtypes = []

ff_get_response = api.ff_get_response
ff_get_response.restype = c_char_p
ff_get_response.argtypes = []

fo_unsettled_qty = api.fo_unsettled_qry
fo_unsettled_qty.restype = c_char_p
fo_unsettled_qty.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p,
                             c_char_p, c_char_p, c_char_p, ]

fo_order_qry = api.fo_order_qry
fo_order_qry.restype = c_char_p
fo_order_qry.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p,
                         c_char_p, c_char_p, ]

fo_order_qry2 = api.fo_order_qry2
fo_order_qry2.restype = c_char_p
fo_order_qry2.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p,
                          c_char_p, c_char_p, c_char_p, ]

ff_get_info = api.ff_get_info
ff_get_info.restype = c_char_p
ff_get_info.argtypes = [c_char_p, c_char_p, ]

stock_balance_qry = api.stock_balance_qry
stock_balance_qry.restype = c_char_p
stock_balance_qry.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p,
                              c_char_p, ]

stock_balance_sum = api.stock_balance_sum
stock_balance_sum.restype = c_char_p
stock_balance_sum.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p, ]

stock_balance_detail = api.stock_balance_detail
stock_balance_detail.restype = c_char_p
stock_balance_detail.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p, ]

ff_get_positions = api.ff_get_positions
ff_get_positions.restype = c_char_p
ff_get_positions.argtypes = [c_char_p, c_char_p, ]

ff_order_qry = api.ff_order_qry
ff_order_qry.restype = c_char_p
ff_order_qry.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, ]

fo_get_day_info = api.fo_get_day_info
fo_get_day_info.restype = c_char_p
fo_get_day_info.argtypes = [c_char_p, c_char_p, ]

fo_get_hist_info = api.fo_get_hist_info
fo_get_hist_info.restype = c_char_p
fo_get_hist_info.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p, ]

# API Part iv.
get_response_log = api.get_response_log
get_response_log.restype = c_char_p
get_response_log.argtypes = []

check_response_buffer = api.check_response_buffer
check_response_buffer.restype = c_int
check_response_buffer.argtypes = []

timer_response_log = api.timer_response_log
timer_response_log.restype = c_char_p
timer_response_log.argtypes = []

get_response_evt = api.get_response_evt
get_response_evt.restype = HANDLE
get_response_evt.argtypes = []

fifo_response = api.fifo_response
fifo_response.restype = c_int
fifo_response.argtypes = []

# API part v.
change_echo = api.change_echo
change_echo.restype = c_char_p
change_echo.argtypes = []

log_out = api.log_out
log_out.restype = c_int
log_out.argtypes = []

show_version = api.show_version
show_version.restype = c_char_p
show_version.argtypes = []

show_list = api.show_list
show_list.restype = c_char_p
show_list.argtypes = []

show_list2 = api.show_list2
show_list2.restype = c_char_p
show_list2.argtypes = []

show_ip = api.show_ip
show_ip.restype = c_char_p
show_ip.argtypes = []

do_register = api.do_register
do_register.restype = c_int
do_register.argtypes = [c_int]


def decorate_to_utf8(func):
    """只要參數是str就要to cp950給t4.dll
    只要回傳值是bytes就要to utf8給 Api caller"""

    def func_wrapper(*args):
        new_args = list(args)
        for idx, arg in enumerate(args):
            if isinstance(arg, str):
                new_args[idx] = args[idx].encode('utf-8')

        res = func(*new_args)
        if isinstance(res, bytes):
            return str(res, 'cp950')
        else:
            return res

    return func_wrapper


class T4(object):
    @classmethod
    @decorate_to_utf8
    def init_t4(cls, *args):
        return init_t4(*args)

    @classmethod
    @decorate_to_utf8
    def show_ip(cls, *args):
        return show_ip(*args)

    @classmethod
    @decorate_to_utf8
    def show_version(cls):
        return show_version()

    @classmethod
    @decorate_to_utf8
    def do_register(cls, reg):
        return do_register(reg)

    @classmethod
    @decorate_to_utf8
    def add_acc_ca(cls, branch, account, account_id, ca_path, ca_password):
        return add_acc_ca(branch, account, account_id, ca_path, ca_password)

    @classmethod
    @decorate_to_utf8
    def show_list(cls):
        return show_list()

    @classmethod
    @decorate_to_utf8
    def show_list2(cls):
        return show_list2()

    @classmethod
    @decorate_to_utf8
    def init_t4(cls, *args):
        return init_t4(*args)

    @classmethod
    @decorate_to_utf8
    def add_acc_ca(cls, *args):
        return add_acc_ca(*args)

    @classmethod
    @decorate_to_utf8
    def verify_ca_pass(cls, *args):
        return verify_ca_pass(*args)

    @classmethod
    @decorate_to_utf8
    def stock_order(cls, *args):
        """委託回報為bytes。所以先轉為有結構的NameTuple，但每個item得從bytes to utf8"""
        stock_order_res = stock_order(*args)
        stock_record_field = 'trade_type, Account,stock_id, ord_price, ord_qty, ord_seq, ord_date, effective_date, ord_time,' \
                             'ord_no,ord_soruce,org_ord_seq,ord_bs,ord_type1,ord_type2,market_id,price_type,ord_status,Msg'
        StockOrderRecord = namedtuple('StockOrderRecord', stock_record_field)
        StockOrderRecordfmt = '2s15s6s6s3s6s8s8s6s5s3s6s1s1s1s1s1s2s60s'
        stock_order_res = StockOrderRecord._make(struct.unpack_from(StockOrderRecordfmt, stock_order_res))
        new_vaule = [str(item, 'cp950') for item in stock_order_res]
        return StockOrderRecord(*new_vaule)

    @classmethod
    @decorate_to_utf8
    def stock_cancel(cls, *args):
        return stock_cancel(*args)

    @classmethod
    @decorate_to_utf8
    def future_order(cls, *args):
        return future_order(*args)

    @classmethod
    @decorate_to_utf8
    def future_cancel(cls, *args):
        return future_cancel(*args)

    @classmethod
    @decorate_to_utf8
    def future_change(cls, *args):
        return future_change(*args)

    @classmethod
    @decorate_to_utf8
    def option_order(cls, *args):
        return option_order(*args)

    @classmethod
    @decorate_to_utf8
    def option_cancel(cls, *args):
        return option_cancel(*args)

    @classmethod
    @decorate_to_utf8
    def ffuture_order(cls, *args):
        return ffuture_order(*args)

    @classmethod
    @decorate_to_utf8
    def ffuture_cancel(cls, *args):
        return ffuture_cancel(*args)

    @classmethod
    @decorate_to_utf8
    def get_response(cls, *args):
        return get_response(*args)

    @classmethod
    @decorate_to_utf8
    def ff_get_response(cls, *args):
        return ff_get_response(*args)

    @classmethod
    @decorate_to_utf8
    def fo_unsettled_qty(cls, *args):
        return fo_unsettled_qty(*args)

    @classmethod
    @decorate_to_utf8
    def fo_order_qry(cls, *args):
        return fo_order_qry(*args)

    @classmethod
    @decorate_to_utf8
    def fo_order_qry2(cls, *args):
        return fo_order_qry2(*args)

    @classmethod
    @decorate_to_utf8
    def ff_get_info(cls, *args):
        return ff_get_info(*args)

    @classmethod
    @decorate_to_utf8
    def stock_balance_qry(cls, *args):
        return stock_balance_qry(*args)

    @classmethod
    @decorate_to_utf8
    def stock_balance_sum(cls, *args):
        return stock_balance_sum(*args)

    @classmethod
    @decorate_to_utf8
    def stock_balance_detail(cls, *args):
        return stock_balance_detail(*args)

    @classmethod
    @decorate_to_utf8
    def ff_get_positions(cls, *args):
        return ff_get_positions(*args)

    @classmethod
    @decorate_to_utf8
    def ff_order_qry(cls, *args):
        return ff_order_qry(*args)

    @classmethod
    @decorate_to_utf8
    def fo_get_day_info(cls, *args):
        return fo_get_day_info(*args)

    @classmethod
    @decorate_to_utf8
    def fo_get_hist_info(cls, *args):
        return fo_get_hist_info(*args)

    @classmethod
    @decorate_to_utf8
    def get_response_log(cls, *args):
        return get_response_log(*args)

    @classmethod
    @decorate_to_utf8
    def check_response_buffer(cls, *args):
        return check_response_buffer(*args)

    @classmethod
    @decorate_to_utf8
    def timer_response_log(cls, *args):
        return timer_response_log(*args)

    @classmethod
    @decorate_to_utf8
    def get_response_evt(cls, *args):
        return get_response_evt(*args)

    @classmethod
    @decorate_to_utf8
    def fifo_response(cls, *args):
        return fifo_response(*args)

    @classmethod
    @decorate_to_utf8
    def change_echo(cls, *args):
        return change_echo(*args)

    @classmethod
    @decorate_to_utf8
    def log_out(cls, *args):
        return log_out(*args)


if __name__ == '__main__':
    with open('../OrderAPI.json') as fd_json:
        UserInfo = json.load(fd_json)
    msg = T4.init_t4(UserInfo['UserId'], UserInfo['Password'], '')
    print(msg)
    print(T4.show_version())
    print(T4.show_ip())
    print(T4.show_list())
    print(T4.do_register(1))
    print(T4.show_list2())
