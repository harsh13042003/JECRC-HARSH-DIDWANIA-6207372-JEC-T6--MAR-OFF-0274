*** Settings ***
Resource    ../../resource/pages/sign_up_page.robot
Resource    ../../resource/common_resources.robot
Suite Setup    Load Environment
Test Setup    Open Applications
Test Teardown    CLose Applications

*** Test Cases ***
TC01 Register User
    [Documentation]    Checking if the user can register or not
    [Tags]    functional
    Sign Up To The Application    JONY        MONY    jededrdfrogtfrs@gmail.com    passsss123