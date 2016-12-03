# coding=utf-8
# __author__ == ypochien at gmail.com

from ctypes import *
from ctypes.wintypes import *

api = windll.LoadLibrary("OrderAPI/pyT4/t4.dll")

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

if __name__ == '__main__':
    print(show_version())
    print(show_ip())
    print(show_list())
