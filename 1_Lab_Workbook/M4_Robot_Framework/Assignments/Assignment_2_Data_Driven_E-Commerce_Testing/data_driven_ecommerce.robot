*** Settings ***
Resource    resources/ecommerce_keywords.resource

Test Setup       Open E-Commerce Website
Test Teardown    Close E-Commerce Website
Test Template    Search Product And Verify


*** Test Cases ***
Search Laptop       laptop
Search Book         book
Search Computer     computer


*** Keywords ***
Search Product And Verify
    [Arguments]    ${product}

    Search Product    ${product}
    Verify Search Result    ${product}
