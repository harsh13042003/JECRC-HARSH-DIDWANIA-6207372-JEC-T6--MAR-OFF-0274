*** Settings ***
Documentation    levels of login
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.cricbuzz.com/

*** Test Cases ***
handling login
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Log    navigated to cricbuzz    ERROR
    Log To Console    navigated to cricbuzz
    Sleep    3s
    Close Browser

## robot -d reports --timestampoutputs open_browser.robot    --> correct one
## robot -d reports/$(Get-Date-Format 'yyyy-MM-dd_HH-mm-ss') <filename>    --> correct one
## arguments in python:
## positional, default, keyword arguments
## whenever calling a function and passing arguments it becomes keyword arguments eg. name(first='abc', last='xyz')