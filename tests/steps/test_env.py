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
    context.account_list = context.api.get_account_list()


@then("會得到{nums:d}個交易帳號")
def step_impl(context, nums):
    assert_that(nums, equal_to(len(context.account_list)))
