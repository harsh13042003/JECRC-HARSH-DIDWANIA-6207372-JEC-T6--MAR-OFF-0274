*** Settings ***
Library    SeleniumLibrary
Resource    ../../locators/login_locators.robot

*** Keywords ***
log In To The Application
    [Documentation]   loging in to the application
    [Arguments]    ${login_email}    ${pwd}
    Input Text    ${login_link}    ${login_email}
    Log    login mail
    Input Text    ${login_pw}    ${pwd}
    Log   password
    Click Element    ${login_btn}
    Log    Clicking  login button
