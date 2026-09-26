# Wipro Selenium Automation

Coursework, capstone project, and certifications completed as part of the
**Wipro Selenium Python Automation** program — covering Selenium WebDriver,
unit testing frameworks, BDD, REST API automation, and Robot Framework.

## Repository Structure

```
Wipro_Selenium_Automation/
├── 1_Lab_Workbook/           # Module-wise lab experiments and assignments
│   ├── M1_Selenium_Automation/
│   ├── M2_Unit_Test_Frameworks/
│   ├── M3_Python_BDD_Restful_Automation/
│   └── M4_Robot_Framework/
├── 2_Capstone_Project/       # Final project: API automation framework
│   ├── Project_Report/
│   └── api-automation-framework/
└── 3_Certificates/           # Program completion certificates
```

## 1. Lab Workbook

Module-wise lab experiments and assignments, each with a problem statement,
objective, source code, output screenshots, and observations.

| Module | Topics | Assignments |
|---|---|---|
| **M1 — Selenium Automation** | WebDriver setup, locators, XPath/CSS selectors, navigation, alerts, frames/windows, mouse & keyboard actions, web tables, waits, screenshots, exception handling, JS execution | 6 |
| **M2 — Unit Test Frameworks** | `unittest`, PyTest, Page Object Model (POM) | 3 |
| **M3 — Python BDD & REST Automation** | Python HTTP libraries, API automation, HTTP response handling, BDD with Behave | 3 |
| **M4 — Robot Framework** | Setup and running options, keyword-driven and data-driven testing | 2 |

Each assignment folder is self-contained, with its own README, script(s), and
a `screenshots/` folder showing terminal/output proof of execution.

## 2. Capstone Project

A **Python API automation framework** built with `requests`, Behave (BDD),
JSON Schema validation, and Allure reporting, tested against the
**User Management API** of [automationexercise.com](https://automationexercise.com/api)
(create → login-verify → get → update → delete a user), with a reusable
client-layer design proven against a second, independent API
([jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com/)) with
zero code changes — just a config switch.

Highlights:
- Layered "API Object Model" design — step definitions never call `requests`
  directly, only reusable client methods (`user_client.create_account(...)`)
- Contract validation via JSON Schema, not just status-code checks
- Config-driven environments (`config/config.yaml`) for switching APIs/timeouts
  with a one-line change
- Automatic retry logic on connection errors, timeouts, and 5xx responses
- Allure reports with full request/response bodies attached to every step
- Result: 3 features, 5 scenarios, 26 steps — 100% pass rate

See [`2_Capstone_Project/api-automation-framework/README.md`](2_Capstone_Project/api-automation-framework/README.md)
for full setup and run instructions, and `Project_Report/` for the written
project report.

## 3. Certificates

Completion certificates issued for the program, included as PDFs:
- `PythonforAutomation.pdf`
- `SeleniumWebdriverusingpython.pdf`
- `TestAutomationwithplaywright&robotframework.pdf`

## Tech Stack

Python · Selenium WebDriver · unittest · PyTest · Behave (BDD) · Robot Framework · Requests · JSON Schema · Allure

## Author

**Simantini Das** — [Simantini06](https://github.com/Simantini06)