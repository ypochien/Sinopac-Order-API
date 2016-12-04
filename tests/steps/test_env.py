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


@given(u'建立委託單{stock}股票{qty:d}張{price:f}元')
def step_impl(context, stock, qty, price):
    context.stock = stock
    context.qty = str(abs(qty))
    context.price = str(price)
    context.orders = context.api.make_stock_orders(stock, qty, price)


@when("執行下單委託")
def step_impl(context):
    acc = context.api.accounts['S'][1]
    orders = context.orders
    context.result = context.api.placing_order(acc, orders)


@then("我們會得到此筆委託單的委託回報")
def step_impl(context):
    assert_that(context.stock, equal_to(context.result.stock_id.strip()))
