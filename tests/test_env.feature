# Created by ypochien at 2016/12/2
Feature: 確保下單API可以用
  使用下單API，做基本操作，證明下單API是可以用的


  Scenario: 正常登入
    Given OrderAPI設定檔-"OrderAPI.json"
    When 我們建立OrderAPI
    Then 會收到正常登入的訊息