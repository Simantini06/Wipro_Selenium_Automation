# Wipro Selenium Python Automation — My Coursework & Capstone

This repo holds everything I built during Wipro's Selenium Python Automation
program: hands-on lab assignments across four modules, my final capstone
(a Python API test automation framework), the written project report, and
my program certificates.

## What's in here

```
Wipro_Selenium_Automation/
├── 1_Lab_Workbook/           # My module-wise lab assignments
│   ├── M1_Selenium_Automation/
│   ├── M2_Unit_Test_Frameworks/
│   ├── M3_Python_BDD_Restful_Automation/
│   └── M4_Robot_Framework/
├── 2_Capstone_Project/
│   ├── Project_Report/                 # Written report (PDF)
│   └── api-automation-framework/       # The actual framework code
└── 3_Certificates/           # My program completion certificates
```

## Capstone: Python API Automation Framework

My capstone is an API test automation framework I built with `requests`,
Behave (BDD), JSON Schema, and Allure. It's driven end-to-end against the
**User Management API** on [automationexercise.com](https://automationexercise.com/api) —
covering the full account lifecycle: create → verify login → get → update →
delete.

To prove the design wasn't hardcoded to one API, I pointed the same client
architecture at a completely different service —
[jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com/) —
by changing one config value, no code edits.

**A few design decisions I made and why:**
- Step definitions don't touch `requests` directly — they only call methods
  on a `UserClient` (create_account, verify_login, etc). Kept the Gherkin
  readable and meant if an endpoint ever changes, I fix it in one place
  instead of hunting through step files.
- `automationexercise.com` actually returns HTTP 200 for almost everything —
  the real result is buried inside a `responseCode` field in the JSON body
  (200/201/400/404). Took me a bit to notice this, so my assertions check
  that field instead of `response.status_code`.
- Base URL and timeouts live in `config.yaml`, not hardcoded anywhere. This
  is also how I proved the framework isn't tied to one API — swapping to
  `jsonplaceholder.typicode.com` for the reusability demo was a one-line
  config change, zero code touched.
- Added a retry decorator on the base client for connection errors, timeouts,
  and 5xx responses — but not 4xx, since a 404 or 400 is the API telling you
  something's actually wrong, not just being flaky.
- Responses get validated against a JSON Schema, not just checked for status
  code, so "test passed" actually means the response shape held up too.
- Every request/response pair gets attached to the Allure report automatically
  through a Behave hook — saved me a lot of "wait, what did I even send?"
  moments while debugging failures.

**Result:** 3 feature files, 5 scenarios, 26 steps — all passing.

Full setup/run instructions are in
[`2_Capstone_Project/api-automation-framework/README.md`](2_Capstone_Project/api-automation-framework/README.md).
The write-up with architecture diagrams, screenshots, and test results is in
`2_Capstone_Project/Project_Report/Capstone_Project_Report.pdf`.

## Lab Workbook

Assignments from all four modules of the program, each with the problem
statement, my solution code, and output screenshots.

| Module | What it covers | # Assignments |
|---|---|---|
| M1 — Selenium Automation | WebDriver setup, locators, alerts, frames/windows, waits, web tables, JS execution | 6 |
| M2 — Unit Test Frameworks | `unittest`, PyTest, Page Object Model | 3 |
| M3 — Python BDD & REST Automation | HTTP requests in Python, API testing, Behave BDD | 3 |
| M4 — Robot Framework | Keyword-driven & data-driven testing | 2 |

## Certificates

- `PythonforAutomation.pdf`
- `SeleniumWebdriverusingpython.pdf`
- `TestAutomationwithplaywright&robotframework.pdf`

## Tools & Tech

Python, Selenium WebDriver, unittest, PyTest, Behave, Robot Framework, Requests, JSON Schema, Allure

## Author

Simantini Das — [github.com/Simantini06](https://github.com/Simantini06)