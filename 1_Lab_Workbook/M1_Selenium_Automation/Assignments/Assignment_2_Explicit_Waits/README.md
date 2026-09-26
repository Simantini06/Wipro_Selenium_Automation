# Assignment 2 – Synchronization & Explicit Waits

## Module
M1 – Automation with Selenium

## Experiment Title
Synchronization & Explicit Waits

## Problem Statement
Automate web elements on the Test Automation Practice website using Selenium Explicit Waits.

The automation should wait for web elements to become available before interacting with them instead of using fixed delays such as `time.sleep()`.

## Objective

- Understand synchronization in Selenium.
- Understand the purpose of Explicit Waits.
- Use `WebDriverWait` in Selenium Python.
- Use Expected Conditions to wait for web elements.
- Use `visibility_of_element_located()`.
- Use `element_to_be_clickable()`.
- Avoid fixed delays such as `time.sleep()`.

## Tools / Software

- Python
- Selenium WebDriver
- Chrome Browser
- WebDriver Manager
- Test Automation Practice website

## Concepts Used

- Selenium WebDriver
- Explicit Wait
- `WebDriverWait`
- Expected Conditions
- `visibility_of_element_located()`
- `element_to_be_clickable()`
- `By.ID`
- `send_keys()`

## Website Used

Test Automation Practice:

https://testautomationpractice.blogspot.com/

## Implementation

The automation script performs the following steps:

1. Launches the Chrome browser.
2. Opens the Test Automation Practice website.
3. Maximizes the browser window.
4. Creates an Explicit Wait using `WebDriverWait`.
5. Waits until the Name field becomes visible.
6. Enters a name into the Name field.
7. Waits until the Email field becomes clickable.
8. Enters an email address into the Email field.
9. Displays successful execution messages in the console.
10. Closes the browser.

## Result

The web elements were successfully identified and interacted with using Selenium Explicit Waits.

## Observation

Explicit Wait allows Selenium to wait for a specific condition before interacting with an element.
It is more flexible than using a fixed delay because the script can continue immediately when the required condition is satisfied.

## Conclusion

The experiment successfully demonstrates synchronization using WebDriverWait and Selenium Expected Conditions.

```python
wait = WebDriverWait(driver, 10)
