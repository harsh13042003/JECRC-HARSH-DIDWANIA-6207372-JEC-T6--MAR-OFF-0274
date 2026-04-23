*** Settings ***
Library    SeleniumLibrary
Resource    ../../locators/prod_catalog_locator.robot

*** Keywords ***
Product Search
    [Documentation]    searching  clicking on the product
    [Arguments]    ${search}

    Click Element    ${search_link}
    Log    clicking search field
    
    Input Text    ${search_link}    ${search}
    Log    searching item 
    
    Click Element    ${search_button}
    Log    clicking search button

    Wait Until Element Is Visible    ${item_1}    12s
    Click Element    ${item_1}
    Log    clicking first item

    Sleep    3s