# Assignment 7 – Selenium with Unittest

## Module
**M2 – Unit Test Frameworks**

## Experiment Title
**Selenium Automation using Python Unittest Framework**

## Problem Statement
Create automated test cases using Python's `unittest` framework and Selenium WebDriver. The test cases should verify important properties of a web page such as its title, URL, and visibility of a page element.

## Objective
- Understand the Python `unittest` framework.
- Create Selenium test cases using `unittest.TestCase`.
- Use `setUp()` and `tearDown()` methods.
- Perform assertions using `assertIn()` and `assertTrue()`.
- Execute multiple Selenium test cases as a test suite.

## Website Used
**Test Automation Practice**

`https://testautomationpractice.blogspot.com/`

## Tools / Software / Concepts
- Python
- Selenium WebDriver
- Chrome Browser
- WebDriver Manager
- Python Unittest
- Selenium Locators
- XPath
- Assertions
- `setUp()`
- `tearDown()`

## Implementation

### 1. Browser Setup
The Chrome browser is initialized using Selenium WebDriver and WebDriver Manager.

### 2. setUp()
The `setUp()` method:
- Opens the Chrome browser.
- Navigates to the Test Automation Practice website.
- Maximizes the browser window.

### 3. Test Cases

Three test cases were created:

#### Test Case 1 – Verify Page Title
The page title is retrieved using:

```python
self.driver.title
```

The title is verified using:

```python
self.assertIn("Automation Testing Practice", title)
```

#### Test Case 2 – Verify Page URL
The current URL is retrieved using:

```python
self.driver.current_url
```

The URL is verified using:

```python
self.assertIn("testautomationpractice.blogspot.com", url)
```

#### Test Case 3 – Verify Heading Visibility
The page heading is located using XPath and its visibility is checked using:

```python
self.assertTrue(logo.is_displayed())
```

### 4. tearDown()
The tearDown() method closes the browser after each test using:

```python
self.driver.quit()
```

## Source Code

The complete Selenium implementation is available in:
```assignment7.py```

## Output
The test execution produced:

Logo/Heading is displayed
.Page Title: Automation Testing Practice
.Page URL: https://testautomationpractice.blogspot.com/
.
----------------------------------------------------------------------
Ran 3 tests in 48.581s

OK

All 3 test cases passed successfully.

## Result

Successfully implemented Selenium automation using Python's unittest framework.
Three test cases were executed successfully for page title, page URL, and heading visibility.

## Observation

1. unittest.TestCase was used to create the test class.
2. Methods beginning with test_ were automatically identified as test cases.
3. setUp() was used for browser initialization.
4. tearDown() was used to close the browser.
5. Assertions were used to validate test conditions.
6. All three test cases passed successfully.

## Conclusion

The experiment provided practical understanding of integrating Selenium WebDriver with Python's unittest framework. It demonstrated test setup, multiple test cases, assertions, and cleanup using setUp() and tearDown().
