# Assignment 3 – Selenium POM + Behave + Gherkin

## Module

M3 – Python BDD Restful Automations

## Experiment Title

Selenium Page Object Model using Behave and Gherkin

## Problem Statement

To implement Selenium web automation using the Page Object Model (POM) with Behave BDD and Gherkin syntax.

## Objective

- To integrate Selenium with Behave.
- To implement the Page Object Model.
- To separate page locators and actions from step definitions.
- To write web automation scenarios using Gherkin.
- To validate form data using reusable page methods.
- To demonstrate a structured BDD automation framework.

## Tools and Technologies

- Python
- Selenium WebDriver
- Behave
- WebDriver Manager
- Gherkin
- Page Object Model
- Google Chrome

## Project Structure

```text
ass_3/
├── features/
│   ├── steps/
│   │   └── login_steps.py
│   └── login.feature
├── pages/
│   └── login_page.py
├── screenshots/
│   ├── assignment_3_success.png
│   └── terminal_success.png
├── README.md
└── requirements.txt
```

## Application Under Test

Test Automation Practice:
https://testautomationpractice.blogspot.com/

## Page Object Model

The LoginPage class contains:

1. Web element locators
2. Methods for entering name
3. Methods for entering email
4. Methods for entering phone number
5. Method for selecting male gender
6. Methods for retrieving entered values
7. Method for checking gender selection

The step definitions interact with the page through these methods instead of directly managing the locators.

## Execution

Open PowerShell in the ass_3 directory and run:

```text
behave --no-capture
```

## Actual Result

The automation executed successfully.

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
6 steps passed, 0 failed, 0 skipped

## Source Code

```python
login_steps.py
login_page.py
```

## Output

The following operations were successfully performed:

1. Automation Practice website opened
2. Name entered through POM
3. Email entered through POM
4. Phone number entered through POM
5. Male gender selected through POM
6. Form data validated successfully
7. Browser closed after execution

## Result

Selenium POM integration with Behave and Gherkin was successfully implemented.

## Observation

The Page Object Model separates web-page locators and actions from the Behave step definitions. This makes the automation code more organized and reusable.

## Conclusion

The Selenium Page Object Model was successfully integrated with Behave BDD. A Gherkin scenario was used to describe the test flow, while the Page Object class handled Selenium locators and browser interactions.
