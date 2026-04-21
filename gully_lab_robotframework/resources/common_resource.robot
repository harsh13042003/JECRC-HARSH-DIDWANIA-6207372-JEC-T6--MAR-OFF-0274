*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}    FireFox

*** Keywords ***
Load Environment
    ${url}=    Get Env    baseurl
    ${email}=    Get Env    user_email
    ${pwd}=    Get Env    user_password

Open Applications
    [Documentation]    Opening the application on browser
    [Arguments]    ${url}
    Open Browser    ${url}    ${BROWSER}
    Maximize Browser Window

Close Applications
    Close All Browsers