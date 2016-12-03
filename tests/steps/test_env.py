import os

from behave import *
from hamcrest import assert_that, equal_to, is_not

from OrderAPI import OrderAPI


@given('OrderAPI設定檔-"{config_file}"')
def step_impl(context, config_file=None):
    context.config_file = config_file


@when("我們建立OrderAPI")
def step_impl(context):
    context.api = OrderAPI.OrderAPI(context.config_file)


@then("會收到{msg}的訊息")
def step_impl(context, msg):
    assert_that(msg, equal_to(context.api.status))


@then("可以得到設定檔的{msg}")
def step_impl(context, msg):
    assert_that(msg, equal_to(context.api.server_ip))
