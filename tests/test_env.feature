# Created by ypochien at 2016/12/2
Feature: 確保下單API可以用
  使用下單API，做基本操作，證明下單API是可以用的


  Scenario: 建立OrderAPI，並初始化t4
    Given OrderAPI設定檔-"OrderAPI/OrderAPI.json"
    When 我們建立OrderAPI
    Then 會收到初始化成功的訊息
    And 可以得到T4的"eleader.sinotrade.com.tw:443"
