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
    assert_that(nums, equal_to(len(context.account_list['S'])))


@given(u'建立委託單"{stock}"股票"{qty:n}"張"{price:f}"元')
def step_impl(context, stock, qty, price):
    context.stock = stock
    context.qty = str(abs(qty))
    context.price = str(price)
    context.orders = context.api.make_stock_orders(stock, qty, price)


@when("執行下單委託")
def step_impl(context):
    acc = context.api.accounts['S'][0]
    orders = context.orders
    context.result = context.api.placing_order(acc, orders)


@then("我們會得到此筆委託單的委託回報")
def step_impl(context):
    assert_that(context.stock, equal_to(context.result['stock_id'].strip()))


@step("將刪單此筆委託")
def step_impl(context):
    cancel_items = (
        ('bs', context.result['ord_bs']),
        ('branch', context.result['Account'][1:5]),  # [S9A95   0483976]
        ('account', context.result['Account'][8:15]),
        ('stock', context.result['stock_id']),
        ('ord_type', context.result['ord_type']),
        ('ord_seq', context.result['ord_seq']),
        ('ord_no', context.result['ord_no']),
        ('pre_order', ' ' if context.result['ord_no'] == '00000' else 'N'))
    cancel_stock_order = OrderedDict(cancel_items)
    orders = context.api.placing_cancel_order(cancel_stock_order)
    print(orders)
    assert_that(0, equal_to(0))
