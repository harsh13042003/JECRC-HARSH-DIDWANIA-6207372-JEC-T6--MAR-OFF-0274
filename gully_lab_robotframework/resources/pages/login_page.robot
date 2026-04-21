*** Settings ***
Library    SeleniumLibrary
Resource    ../../locators/login_page_locator.robot

*** Keywords ***
Login Page
    [Documentation]    Login  page
    [Arguments]    ${mail}    ${pwd}

    Sleep    3s
    Input Text    ${email}    ${mail}
    Log    Entering  mail

    Input Text    ${password}    ${pwd}
    Log    Entering  password

    Click Element    ${signin_btn}
    Log    Clicking  sign in button

    Page Should Contain Element    xpath=//a[text()='Log out']
    Page Should Contain Element    xpath=//h1[text()='Account']
    Sleep    3s 