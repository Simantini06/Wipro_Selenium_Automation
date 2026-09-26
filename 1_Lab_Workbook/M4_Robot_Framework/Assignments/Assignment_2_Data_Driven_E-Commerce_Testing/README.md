# M4 Assignment 2 – Data-Driven E-Commerce Testing

## Module
M4 – Robot Framework Web Automation

## Assignment Title
Data-Driven E-Commerce Testing using Robot Framework

## Problem Statement

Automate product search functionality of an e-commerce website using
Robot Framework while avoiding duplicate automation code.

## Objective

The objective of this assignment is to:

- Use Robot Framework with SeleniumLibrary
- Create reusable user-defined keywords
- Use Resource Files
- Implement keyword arguments
- Implement data-driven testing
- Use Test Template
- Automate multiple product searches
- Capture screenshots
- Generate Robot Framework reports

## Application Used

Demo Web Shop

URL:

https://demowebshop.tricentis.com/

## Tools and Technologies

- Python
- Robot Framework
- SeleniumLibrary
- Selenium WebDriver
- Google Chrome
- Visual Studio Code
- PowerShell

## Project Structure

```text
ass_2/
├── resources/
│   └── ecommerce_keywords.resource
├── screenshots/
│   ├── laptop_search.png
│   ├── book_search.png
│   └── computer_search.png
├── data_driven_ecommerce.robot
├── README.md
├── requirements.txt
├── output.xml
├── log.html
└── report.html
```

## Robot Framework Concepts Used

1. Resource Files
2. SeleniumLibrary
3. User-defined Keywords
4. Keyword Arguments
5. Test Setup
6. Test Teardown
7. Test Template
8. Data-Driven Testing
9. Variables
10. ID Locator
11. XPath Locator
12. Assertions
13. Screenshot Capture

## Resource File

The reusable Selenium keywords are stored in:
resources/ecommerce_keywords.resource

This allows the main Robot test file to reuse common browser and search operations.

## Data-Driven Testing

The test uses:

Test Template    Search Product And Verify

The following test data is used:

Test Case	Product
Search Laptop	laptop
Search Book	book
Search Computer	computer

The same automation keyword is executed with different product values.

## Test Cases
### Test Case 1 – Search Laptop

Searches for laptop and verifies the search result.

### Test Case 2 – Search Book

Searches for book and verifies the search result.

### Test Case 3 – Search Computer

Searches for computer and verifies the search result.

## Execution Command

Run the following command from the assignment directory:

robot data_driven_ecommerce.robot

## Execution Result
3 tests, 3 passed, 0 failed
Reports Generated

## Robot Framework generated:

output.xml
log.html
report.html

## Result

All three data-driven test cases executed successfully.

3 tests, 3 passed, 0 failed

## Conclusion

This assignment demonstrated data-driven web automation using Robot Framework.

Reusable keywords were separated into a Resource File, while the Test Template
allowed the same automation logic to be executed with multiple product values.
This reduced duplicate automation code and demonstrated reusable keyword-driven
testing.
