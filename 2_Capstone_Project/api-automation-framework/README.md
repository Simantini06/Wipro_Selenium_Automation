# API Automation Framework — Python + Requests + Behave BDD + Allure

Automates the **User Management API** of https://automationexercise.com/api
(create / login-verify / get / update / delete a user), written as
Behave BDD scenarios, with Allure reporting and a reusable client-layer
design that also works against a second API (JSONPlaceholder) with zero
code changes — just a config switch.

## What's inside

```
api-automation-framework/
├── requirements.txt
├── behave.ini                     # tells behave to also emit Allure results
├── config/
│   └── config.yaml                # base URLs / timeouts per environment
├── src/
│   ├── config_reader.py           # loads config.yaml, picks active env
│   ├── clients/
│   │   ├── base_client.py         # shared HTTP logic: session, retries, timing
│   │   ├── user_client.py         # AutomationExercise User Management endpoints
│   │   └── jsonplaceholder_client.py  # same base client, different API (proves reuse)
│   ├── schemas/
│   │   └── user_schemas.py        # JSON Schemas for contract validation
│   └── utils/
│       └── retry.py               # retry decorator for flaky/5xx responses
└── features/
    ├── environment.py             # behave hooks + Allure attachment logic
    ├── user_management.feature    # happy-path: full create→login→get→update→delete
    ├── negative_scenarios.feature # data-driven bad-input scenarios
    ├── reusability_demo.feature   # same framework hitting a second API
    └── steps/
        └── user_steps.py          # step definitions
```

No sign-up, no API key needed for either API used here — both are free
public sandboxes.

---

## 1. Prerequisites

- **Python 3.9+** installed (`python --version` or `python3 --version`)
- **Java 8+** installed — *only needed if you want the pretty HTML Allure
  report*. Check with `java -version`. If you don't have it, everything
  still runs and produces raw results; you'll just skip the HTML report step.

---

## 2. Setup (one-time)

Open a terminal in the `api-automation-framework` folder, then:

```bash
# create a virtual environment
python -m venv venv

# activate it
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

# install dependencies
pip install -r requirements.txt
```

---

## 3. Run the tests

```bash
behave
```

That's it. This runs all three feature files against `automationexercise`
(the default environment in `config.yaml`) and writes raw Allure results
into an `allure-results/` folder, plus prints readable pass/fail output
in your terminal.

**Switch environment** (e.g. to prove reusability by pointing the primary
client at JSONPlaceholder too):
```bash
behave -D env=jsonplaceholder
```

**Run just one feature file:**
```bash
behave features/negative_scenarios.feature
```

---

## 4. View the Allure HTML report

You need the Allure command-line tool for this (separate from the Python
packages you just installed — it's a small Java-based CLI).

**Install it (pick one):**
```bash
# macOS
brew install allure

# Windows (with Scoop)
scoop install allure

# Any OS with Node.js installed
npm install -g allure-commandline
```

**Then, from the project folder, after running `behave`:**
```bash
allure serve allure-results
```
This opens the interactive HTML report directly in your browser (no
separate "generate" step needed). Every step shows the exact request sent
and response received — that's the request/response logging built into
`features/environment.py`.

If you'd rather save the report as static files instead of just viewing it:
```bash
allure generate allure-results --clean -o allure-report
allure open allure-report
```

---

## 5. What each feature file demonstrates

| File | Demonstrates |
|---|---|
| `user_management.feature` | Full CRUD lifecycle chained in one scenario (create → verify login → get → update → delete), plus a response-time assertion |
| `negative_scenarios.feature` | Data-driven negative testing via `Scenario Outline` (missing fields, non-existent user) |
| `reusability_demo.feature` | The exact same `BaseAPIClient` design working against JSONPlaceholder, proving the framework isn't hardcoded to one API |

## 6. Design notes (for your report/viva)

- **API Client Layer** (`src/clients/`): step definitions never call
  `requests` directly — they call methods like `user_client.create_account(...)`.
  This is the "API Object Model" pattern, the API-testing equivalent of
  Page Object Model in UI automation.
- **Schema validation** (`src/schemas/`): tests check the *shape* of the
  response (required fields, types), not just the status code.
- **Config-driven environments** (`config/config.yaml`): base URLs and
  timeouts are never hardcoded in code, so adding a new environment or
  API is a one-line config change.
- **Retry logic** (`src/utils/retry.py`): automatically retries on
  connection errors, timeouts, and 5xx responses (not on 4xx, since
  those are deterministic and retrying won't help).
- **Allure request/response logging** (`features/environment.py`):
  every step's exact request and response is attached to the Allure
  report automatically, so a failure shows full context, not just a red X.
