from behave import *
from hamcrest import assert_that, equal_to, is_not

from OrderAPI import OrderAPI


@given('OrderAPI設定檔-"{config_file}"')
def step_impl(context, config_file=None):
    context.config_file = config_file


@when("我們建立OrderAPI")
def step_impl(context):
    context.api = OrderAPI.OrderAPI(context.config_file)


@then("會收到正常登入的訊息")
def step_impl(context):
    assert_that("已登入", equal_to(context.api.status))
