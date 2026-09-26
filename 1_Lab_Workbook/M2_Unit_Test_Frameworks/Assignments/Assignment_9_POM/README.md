# Assignment 9 – Page Object Model (POM)

## Module

M2 – Unit Test Frameworks

## Experiment Title

Implement Page Object Model (POM) using Selenium with Python and PyTest

## Problem Statement

Create a Selenium automation project using the Page Object Model (POM) design pattern.
The automation should separate page-related elements and actions from the test cases. The test should verify the page title, URL, and visibility of the main heading of the Automation Testing Practice website.

## Objective
The objectives of this experiment are:

- To understand the Page Object Model design pattern.
- To separate page locators and page methods from test cases.
- To create a reusable Page Object class.
- To use PyTest for executing Selenium test cases.
- To verify the page title, URL, and heading.
- To improve the maintainability and readability of automation code.

## Website Used
https://testautomationpractice.blogspot.com/

## Tools and Software

- Python 3.10
- Selenium
- PyTest
- WebDriver Manager
- Google Chrome
- Visual Studio Code

## Concepts Used

- Selenium WebDriver
- PyTest
- Fixtures
- Page Object Model (POM)
- XPath
- Assertions
- Browser automation
- WebDriver Manager
- Python classes and methods
- `__init__.py` packages

## Page Object Model Structure
The project separates the page implementation from the test cases.

Test File
    |
    v
HomePage Class
    |
    +---- get_page_title()
    |
    +---- get_page_url()
    |
    +---- get_heading()
    |
    +---- is_heading_displayed()
    |
    v
Automation Testing Practice Website

## Implementation

### 1. Home Page Object
File:
pages/home_page.py

The HomePage class contains the page-related methods.

```python
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.title

    def get_page_url(self):
        return self.driver.current_url

    def get_heading(self):
        return self.driver.find_element(
            By.XPATH,
            "//h1[contains(text(),'Automation Testing Practice')]"
        )

    def is_heading_displayed(self):
        return self.get_heading().is_displayed()
```

### 2. Test File
File:
tests/test_home_page.py

The test file uses the HomePage object instead of directly locating elements inside every test.

```python
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from ass_9.pages.home_page import HomePage


@pytest.fixture
def driver():
    browsername = "chrome"

    if browsername.lower() == "chrome":
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
    elif browsername.lower() == "firefox":
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
    else:
        raise Exception("Invalid browser name.")

    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()

    yield driver

    driver.quit()


def test_page_title(driver):
    home_page = HomePage(driver)

    title = home_page.get_page_title()

    print("Page Title:", title)

    assert "Automation Testing Practice" in title


def test_page_url(driver):
    home_page = HomePage(driver)

    url = home_page.get_page_url()

    print("Page URL:", url)

    assert "testautomationpractice.blogspot.com" in url


def test_heading_displayed(driver):
    home_page = HomePage(driver)

    heading = home_page.get_heading()

    print("Page Heading:", heading.text)

    assert heading.is_displayed()
```

## Test Cases

### Test Case 1 – Verify Page Title
The test retrieves the browser page title through the HomePage class.

Expected:
Automation Testing Practice

### Test Case 2 – Verify Page URL
The test retrieves the current URL through the Page Object.

Expected URL contains:
testautomationpractice.blogspot.com

### Test Case 3 – Verify Page Heading
The test locates the main heading using XPath through the Page Object and verifies that it is displayed.

Expected heading:
Automation Testing Practice

## Test Execution
The tests were executed from the M2 directory using:
pytest ass_9/tests/test_home_page.py -v -s

## Source Code

The complete implementation is available in:
```
home_page.py
test_home_page.py
```

## Output
=================== test session starts ====================

platform win32 -- Python 3.10.0
pytest-9.1.1

collected 3 items

ass_9/tests/test_home_page.py::test_page_title
Page Title: Automation Testing Practice
PASSED

ass_9/tests/test_home_page.py::test_page_url
Page URL: https://testautomationpractice.blogspot.com/
PASSED

ass_9/tests/test_home_page.py::test_heading_displayed
Page Heading: Automation Testing Practice
PASSED

==================== 3 passed in 44.52s ====================

## Result
All three Selenium-PyTest test cases executed successfully.

3 passed

## Observation

1. The Page Object Model successfully separates page-specific implementation from test cases.
2. The HomePage class contains the page methods, while the test file focuses on verification and assertions.
3. This makes the automation project more organized and easier to maintain.

## Conclusion

The Page Object Model was successfully implemented using Selenium with Python and PyTest.
The experiment demonstrated how page elements and actions can be encapsulated inside a Page Object class and reused by multiple test cases.
The final test execution completed successfully with all three tests passing.
