*** Settings ***
Resource    ../resource/common_resources.robot
Library    DataDriver    ../testdata/login_credentials_sauce_data.xlsx    sheet_name=Sheet1    

Test Setup    Open Applications    https://www.saucedemo.com/
Test Teardown    CLose Applications
Test Template    Login to application using excel    

*** Variables ***
${USERNAME}    id=user-name
${PASSWORD}    id=password
${LOGINBTN}    id=login-button

*** Test Cases ***
Excel Data Driven Testing    ${user_creds}    ${pass_creds}
    [Documentation]    data driven testing from excel
    [Tags]    data_driven

*** Keywords ***
Login to application using excel
    [Arguments]    ${user_creds}    ${pass_creds}
    Input Text    ${USERNAME}    ${user_creds}
    Input Text    ${PASSWORD}    ${pass_creds}
    Click Button    ${LOGINBTN}
    
    

