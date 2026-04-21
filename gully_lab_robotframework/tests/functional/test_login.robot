*** Settings ***
Library    SeleniumLibrary
Resource    ../../resources/common_resource.robot
Resource    ../../resources/pages/login_page.robot
Resource    ../../resources/pages/home_page.robot
Resource    ../../resources/pages/logout_page.robot
Resource    ../../resources/pages/search_prod_page.robot

Suite Setup    Open Applications    https://gullylabs.com/
Suite Teardown    Close Applications

*** Test Cases ***
TC01 Login Page
    [Documentation]    Loging  page
    [Tags]    functional
    Home Page
    Login Page    harshagarwal13042003@gmail.com    Harsh@0917

TC02 Logout Function
    [Documentation]    Logout  page
    [Tags]    functional
    Logout Page

TC03 Search Product
    [Documentation]    Searching  product
    [Tags]    Functional
    Home Page
    Login Page        harshagarwal13042003@gmail.com        Harsh@0917
    Sleep    3s
    Search Product    sneakers
    Sleep    3s