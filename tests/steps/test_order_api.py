from collections import OrderedDict

from behave import *
from hamcrest import assert_that, equal_to, is_not

from OrderAPI import OrderAPI


@given('我們建立OrderAPI，使用"{config_file}"')
def step_impl(context, config_file):
    context.api = OrderAPI.OrderAPI(config_file)


@then("會收到{msg}的訊息")
def step_impl(context, msg):
    assert_that(msg, equal_to(context.api.status))


@then('可以得到"{msg}"')
def step_impl(context, msg):
    assert_that(msg, equal_to(context.api.server_ip))


@when("顯示交易帳號")
def step_impl(context):
    context.account_list = context.api.accounts


@then("會得到{nums:d}個交易帳號")
def step_impl(context, nums):
    for item in context.account_list.items():
        print(item)
    assert_that(nums, equal_to(len(context.account_list['S'])))


@given(u'建立委託單"{stock}"股票"{qty:n}"張"{price:f}"元')
def step_impl(context, stock, qty, price):
    context.code = stock
    context.qty = str(abs(qty))
    context.price = str(price)
    context.orders = context.api.make_stock_orders(stock, qty, price)

@when("執行股票下單委託")
def step_impl(context):
    acc = context.api.accounts['S'][0]
    orders = context.orders
    context.result = context.api.placing_order(acc, orders)

@given('建立委託單"{future_id}"期貨"{qty:n}"口"{price:f}"點')
def step_impl(context, future_id, qty, price):
    context.code = future_id
    context.qty = str(abs(qty))
    context.price = str(price)
    context.orders = context.api.make_future_orders(future_id, qty, price)

@when("執行期貨下單委託")
def step_impl(context):
    acc = context.api.accounts['F'][0]
    orders = context.orders
    context.result = context.api.placing_order(acc, orders)


@then("我們會得到此筆委託單的委託回報")
def step_impl(context):
    expected = context.code
    if isinstance(context.result, str):
        res = context.result
    else:
        res = context.result['code_id'].strip()
    assert_that(expected, equal_to(res))


@step("將刪單此筆委託")
def step_impl(context):
    if context.result['account'][0] == 'S':
        cancel_items = (
            ('market_id', 'S'),
            ('bs', context.result['ord_bs']),
            ('branch', context.result['account'][1:5]),  # [S9A95   0483976]
            ('account', context.result['account'][8:15]),
            ('code_id', context.result['code_id']),
            ('ord_type', context.result['ord_type']),
            ('ord_seq', context.result['ord_seq']),
            ('ord_no', context.result['ord_no']),
            ('pre_order', ' ' if context.result['ord_no'] == '00000' else 'N'))
        cancel_order = OrderedDict(cancel_items)
    elif context.result['account'][0] == 'F':
        print('[{}]'.format(context.result['code_id']))
        cancel_items = (
            ('market_id', 'F'),
            ('branch', context.result['account'][1:8]),  # [FF0020009114728]
            ('account', context.result['account'][8:15]),
            ('code_id', context.result['code_id'].strip()),
            ('ord_seq', context.result['ord_seq']),
            ('ord_no', context.result['ord_no']),
            ('oct_type', context.result['oct_type']),
            ('pre_order', ' ' if context.result['ord_no'] == '00000' else 'N'))
        cancel_order = OrderedDict(cancel_items)

    orders = context.api.placing_cancel_order(cancel_order)
    print(orders)
    assert_that(1, equal_to(0))
