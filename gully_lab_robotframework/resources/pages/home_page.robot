*** Settings ***
Library    SeleniumLibrary
Resource    ../../locators/home_page_locator.robot

*** Keywords ***
Home Page
    Click Element    ${account}
    Log    Clicking  account

