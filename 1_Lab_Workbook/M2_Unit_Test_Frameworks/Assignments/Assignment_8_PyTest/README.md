# Assignment 8 – PyTest Framework

## Module

**M2 – Unit Test Frameworks**

## Experiment Title

**PyTest Framework with Selenium, Fixtures and Markers**

## Problem Statement
Develop automated tests using the PyTest framework to validate a web page.

The test should:

- Verify the page title.
- Verify the page URL.
- Verify that the main page heading is displayed.
- Use a PyTest fixture for Selenium WebDriver setup and teardown.
- Use PyTest markers to categorize tests as Smoke and Regression tests.
- Execute selected tests using PyTest markers.

## Objective

The objective of this experiment is to understand and implement:

- PyTest test functions.
- Assertions in PyTest.
- Selenium WebDriver integration with PyTest.
- PyTest fixtures.
- Fixture setup and teardown.
- Custom PyTest markers.
- Smoke testing.
- Regression testing.
- Selective test execution using markers.

## Website Used

**Test Automation Practice**

Website:

https://testautomationpractice.blogspot.com/

## Tools and Software Used

| Tool / Technology | Purpose |
|---|---|
| Python 3.10 | Programming language |
| Selenium | Browser automation |
| PyTest 9.1.1 | Testing framework |
| Chrome Browser | Browser used for execution |
| ChromeDriver | WebDriver for Chrome |
| webdriver-manager | Automatic WebDriver management |
| VS Code / Terminal | Code development and execution |

## Concepts Used
The following concepts were implemented in this experiment:

1. PyTest test functions
2. Assertions
3. Selenium WebDriver
4. PyTest fixtures
5. `yield` in fixtures
6. Fixture teardown
7. `@pytest.mark.smoke`
8. `@pytest.mark.regression`
9. Marker-based test execution
10. Verbose execution using `-v`
11. Console output using `-s`

## Implementation

### Step 1 – Import Required Modules
The required PyTest and Selenium modules are imported.

```python
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
```

### Step 2 – Create the PyTest Fixture
A fixture named driver is created to handle browser setup and cleanup

```python
@pytest.fixture
def driver():
    .
    .
    .
    yield driver
    driver.quit()
```

## Test

### Test Case 1 – Verify Page Title
The first test verifies that the page title contains:

Automation Testing Practice

Implementation:

```python
@pytest.mark.smoke
def test_page_title(driver):
    title = driver.title
    print("Page Title:", title)
    assert "Automation Testing Practice" in title
```

This test is marked as a Smoke Test.

### Test Case 2 – Verify Page URL
The second test verifies that the current URL contains:

testautomationpractice.blogspot.com

Implementation:

```python
@pytest.mark.regression
def test_page_url(driver):
    url = driver.current_url
    print("Page URL", url)
    assert "testautomationpractice.blogspot.com" in url
```

This test is marked as a Regression Test.

### Test Case 3 – Verify Page Heading
The third test locates the main heading using XPath and verifies that it is displayed.

Implementation:

```python
@pytest.mark.regression
def test_heading_displayed(driver):
    heading = driver.find_element(By.XPATH, "//h1[contains(text(),'Automation Testing Practice')]")
    print("Page heading:", heading.text)
    assert heading.is_displayed()
```

This test is also marked as a Regression Test.

## Source Code

The complete implementation is available in:
```assignment_8.py```

## PyTest Configuration
Custom markers were registered in pytest.ini.

pytest.ini
[pytest]
markers =
    smoke: smoke tests
    regression: regression tests

Registering the markers prevents PytestUnknownMarkWarning warnings during execution.

## Test Execution

### Run All Tests

Command:

pytest ass_8.py -v -s

This executes all three test cases.

Expected result:

3 passed

### Run Smoke Tests Only

Command:

pytest ass_8.py -m smoke -v -s

The smoke marker selects only:

test_page_title

Execution result:

collected 3 items / 2 deselected / 1 selected

ass_8.py::test_page_title Page Title: Automation Testing Practice
PASSED

==================== 1 passed, 2 deselected ====================

### Run Regression Tests Only

Command:

pytest ass_8.py -m regression -v -s

The regression marker selects:

test_page_url
test_heading_displayed

Execution result:

collected 3 items / 1 deselected / 2 selected

ass_8.py::test_page_url Page URL https://testautomationpractice.blogspot.com/
PASSED

ass_8.py::test_heading_displayed Page heading: Automation Testing Practice
PASSED

==================== 2 passed, 1 deselected ====================

## Output

### Smoke Test Output

The Smoke test successfully executed only the page-title test.

Result:

1 passed, 2 deselected

### Regression Test Output

The Regression tests successfully executed the page URL and page heading tests.

Result:

2 passed, 1 deselected

## Result
The PyTest automation experiment was successfully completed.

All three Selenium test cases passed successfully:
1. Page title verification – PASSED
2. Page URL verification – PASSED
3. Page heading verification – PASSED

Smoke and Regression tests were also successfully executed using PyTest markers.

## Observation
The following observations were made during the experiment:

1. PyTest allows test cases to be written as simple Python functions.
2. Assertions are used to verify expected results.
3. Fixtures help manage common setup and teardown operations.
4. The Selenium WebDriver can be passed to test functions through a fixture.
5. yield allows the test to execute before the teardown code runs.
6. driver.quit() closes the browser after test execution.
7. PyTest markers can be used to categorize test cases.
8. The -m option allows only selected categories of tests to be executed.
9. The -v option provides detailed test execution information.
10. The -s option displays print() output in the terminal.

## Conclusion
This experiment provided practical experience with the PyTest testing framework and its integration with Selenium.
The experiment successfully demonstrated PyTest fixtures, Selenium WebDriver setup and teardown, assertions, custom markers, Smoke testing, Regression testing, and selective test execution.
Therefore, the objective of the experiment was successfully achieved.
