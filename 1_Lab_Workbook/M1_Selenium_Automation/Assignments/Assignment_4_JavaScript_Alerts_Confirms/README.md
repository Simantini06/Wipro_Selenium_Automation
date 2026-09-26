# Assignment 4 – JavaScript Alerts and Confirms

## Module

**M1 – Automation with Selenium**

## Experiment Title

**JavaScript Alerts and Confirms**

## Problem Statement

Automate JavaScript popups using Selenium WebDriver.

The task is to handle the following types of JavaScript popups:

1. Alert popup – accept the alert.
2. Confirm popup – dismiss the confirmation.
3. Prompt popup – enter text and accept the prompt.

## Objective

The objective of this experiment is to understand and implement JavaScript popup handling using Selenium WebDriver.

This experiment demonstrates:

- Switching to JavaScript alerts using `switch_to.alert`
- Reading alert messages using `alert.text`
- Accepting an alert using `accept()`
- Dismissing a confirmation using `dismiss()`
- Entering text into a prompt using `send_keys()`
- Accepting a prompt after entering text

## Website Used

**Test Automation Practice**

https://testautomationpractice.blogspot.com/

## Tools & Technologies

- Python
- Selenium WebDriver
- Chrome Browser
- WebDriver Manager
- XPath
- JavaScript Alerts
- Selenium WebElements

## JavaScript Popup Types

### 1. Alert

An alert popup displays a message and normally contains an **OK** button.

Selenium handles it using:

```python
alert = driver.switch_to.alert

The message can be read using:
alert.text

The alert can be accepted using:
alert.accept()
```

### 2. Confirm

A confirmation popup normally contains OK and Cancel options.

```python
It can be dismissed using:
confirm.dismiss()
```

### 3. Prompt

A prompt popup allows the user to enter text.

```python
Text can be entered using:
prompt.send_keys("Arpan Mukherjee")

The prompt can then be accepted using:
prompt.accept()
```

## Implementation

1. Open the Website
2. Handle Alert
3. Handle Confirm
4. Handle Prompt

## Source Code

The complete Selenium implementation is available in:
```assignment4.py```

## Output

The program successfully handled all three JavaScript popups.

Terminal Output
Alert Message: I am an alert box!
Alert accepted

Confirm Message: Press a button!
Confirm dismissed

Prompt message: Please enter your name:
Prompt text entered and accepted

## Result

The JavaScript Alert, Confirm, and Prompt popups were successfully automated using Selenium WebDriver.
1. Alert was accepted successfully.
2. Confirm popup was dismissed successfully.
3. Prompt text was entered and accepted successfully.

## Observation

1. Selenium provides switch_to.alert for handling JavaScript popups.
2. alert.text can be used to read the popup message.
3. accept() performs the OK action.
4. dismiss() performs the Cancel action on a confirmation popup.
5. send_keys() can be used to enter text into a prompt.

## Conclusion

This experiment provided practical experience in handling JavaScript Alert, Confirm, and Prompt popups using Selenium with Python.
The required popup operations were successfully performed using Selenium WebDriver.
