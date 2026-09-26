*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${URL}        https://demowebshop.tricentis.com/
${BROWSER}    chrome


*** Keywords ***
Open E-Commerce Website
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Page Should Contain    Demo Web Shop


Search Product
    [Arguments]    ${product}

    Input Text    id=small-searchterms    ${product}
    Click Button    xpath=//input[@value='Search']

    Page Should Contain    Search
    Capture Page Screenshot    screenshots/${product}_search.png


Verify Search Result
    [Arguments]    ${product}

    Page Should Contain    ${product}


Close E-Commerce Website
    Close Browser
