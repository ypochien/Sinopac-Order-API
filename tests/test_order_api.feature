# Created by ypochien at 2016/12/2
Feature: OrderAPI操作
  As a 下單API
  I want 執行基本操作
  So that 下單API是可以用的

  Background: 建立OrderAPI
    Given 我們建立OrderAPI，使用"OrderAPI/OrderAPI.json"

  Scenario: 初始化登入
    Then 會收到初始化成功的訊息
    And 可以得到"eleader.sinotrade.com.tw:443"


  Scenario: 列出可交易帳號
    When 顯示交易帳號
    Then 會得到1個交易帳號


  Scenario Outline: 建立現貨委託單
    Given 建立委託單"<stock>"股票"<qty>"張"<price>"元
    When 執行股票下單委託
    Then 我們會得到此筆委託單的委託回報
    And 將刪單此筆委託
    Examples: Stock_Order
      | stock | qty | price |
      | 2890  | 1   | 8.8   |
      | 2801  | -2  | 16.0  |

  Scenario Outline: 建立期貨委託單
    Given 建立委託單"<future_id>"期貨"<qty>"口"<price>"點
    When 執行期貨下單委託
    Then 我們會得到此筆委託單的委託回報
    And 將刪單此筆委託
    Examples: Future_Order
      | future_id | qty | price  |
      | TXFL6     | -1  | 9371.0 |
      | EXFL6     | 2   | 374.65 |