# Created by ypochien at 2016/12/2
Feature: 非交易面的操作
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
    Then 會得到2個交易帳號
