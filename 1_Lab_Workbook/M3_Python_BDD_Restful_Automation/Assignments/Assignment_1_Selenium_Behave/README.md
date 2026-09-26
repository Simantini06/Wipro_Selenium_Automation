# Assignment 1 – Selenium Python with Behave BDD

## Module
M3 – Python BDD Restful Automations

## Experiment
Selenium Python with Behave BDD

## Problem Statement
Automate a web form using Selenium WebDriver with Python and Behave BDD. 
The test scenario is written using Gherkin syntax and implemented using 
Python step definitions.

## Objective
- Set up Behave with Selenium Python
- Create a Gherkin feature file
- Implement Given, When and Then step definitions
- Automate a web form using Selenium
- Validate the entered form data
- Execute the scenario end-to-end

## Tools and Technologies
- Python 3.10
- Selenium WebDriver
- Behave
- Chrome Browser
- WebDriver Manager
- Gherkin

## Website
https://testautomationpractice.blogspot.com/

## Project Structure

```text
ass_1/
├── features/
│   ├── selenium_form.feature
│   └── steps/
│       └── selenium_steps.py
│
├── screenshots/
│   ├── assignment_1_success.png
│   └── terminal_success.png
│
├── README.md
└── requirements.txt
```

## Test Scenario
The scenario performs the following steps:

1. Open the Automation Practice website.
2. Enter the name.
3. Enter the email.
4. Enter the phone number.
5. Select the male gender.
6. Validate the entered data.

## Execution
Run the following command from the assignment directory:

```
behave --no-capture
```

## Expected Result

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
6 steps passed, 0 failed, 0 skipped

## Source Code

```python
selenium_steps.py
```

## Output

The Selenium script successfully opened the website, entered the required
form information, selected the male gender option, and validated the
entered values.

## Result

The Selenium form automation scenario was executed successfully using
Behave BDD.

## Observation

Behave allows the test scenario to be written in readable Gherkin syntax
while the actual browser automation is implemented separately in Python
step definitions.

## Conclusion

This experiment demonstrated the integration of Selenium WebDriver with
Behave BDD. A complete end-to-end web automation scenario was created,
executed, and validated successfully.
