*** Settings ***
Library    SeleniumLibrary
Resource    ../../locators/home_page_locator.robot

*** Variables ***
${search_bar}    //input[@id='Search-In-Template']

*** Keywords ***
Search Product
    [Documentation]    Search the product in the site
    [Arguments]    ${search_item}
    
    Click Element    ${search}
    Click Element    ${search_bar}
    Input Text    ${search_bar}    ${search_item}

    Press Key    ${search_bar}    ENTER
    Sleep    3s