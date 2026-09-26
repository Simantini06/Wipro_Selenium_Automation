# Assignment 1 – Multi-Locator Challenge

## Module
M1 – Automation with Selenium

## Experiment Title
Multi-Locator Challenge

## Problem Statement
Automate the form available on the Test Automation Practice website using different Selenium locator strategies.

The original assignment specifies a login-page scenario. Since the Test Automation Practice website is being used as the common practice environment, the same locator concepts are demonstrated using the available form elements.

## Objective

- Understand Selenium locators.
- Use different locator strategies to identify web elements.
- Enter data into input fields.
- Select a radio button.
- Verify the entered data and selected state.

## Tools / Software

- Python
- Selenium WebDriver
- Chrome Browser
- WebDriver Manager
- Test Automation Practice website

## Locator Strategies Used

1. By.ID
2. By.NAME
3. By.XPATH

## Implementation

The automation script performs the following steps:

1. Launches Chrome browser.
2. Opens the Test Automation Practice website.
3. Locates the Name field using ID.
4. Enters the name.
5. Locates the Email field using ID.
6. Enters the email address.
7. Locates the Male radio button using XPath.
8. Selects the radio button.
9. Verifies the entered values.
10. Verifies that the radio button is selected.
11. Closes the browser.

## Source Code

See `assignment1.py`.

## Expected Output

The console should display:

Name: Simantini
Email: simantini@example.com
Male selected: False

## Result

The form elements were successfully identified and interacted with using multiple Selenium locator strategies.

## Observation

Different locator strategies can be used depending on the attributes and structure of the web element.

## Conclusion

The experiment successfully demonstrates the use of ID, NAME and XPath locators in Selenium Python automation.
