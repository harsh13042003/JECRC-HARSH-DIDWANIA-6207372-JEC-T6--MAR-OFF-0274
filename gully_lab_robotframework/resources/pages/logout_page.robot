*** Settings ***
Library    SeleniumLibrary
Resource    ../../locators/logout_page_locator.robot

*** Keywords ***
Logout page
    [Documentation]    Logging out page
    Sleep    3s
    Page Should Contain Element    xpath=//a[text()='Log out']

    Click Element    ${logout_btn}
    Sleep    3s