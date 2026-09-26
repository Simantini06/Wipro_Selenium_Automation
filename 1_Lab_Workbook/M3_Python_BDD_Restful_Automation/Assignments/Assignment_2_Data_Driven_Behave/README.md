# Assignment 2 – Data-Driven Python Behave

## Module

M3 – Python BDD Restful Automations

## Experiment Title

Data-Driven API Testing using Python Behave

## Problem Statement

To automate REST API testing using Python Behave with external test data and validate multiple API responses using a single BDD scenario.

## Objective

- To implement data-driven API automation using Behave.
- To read test data from an external JSON file.
- To send GET requests for multiple API endpoints.
- To validate API response status codes.
- To validate returned post IDs.
- To demonstrate reusable BDD automation.

## Tools and Technologies

- Python
- Behave
- Requests
- JSON
- REST API
- PyCharm / VS Code
- JSONPlaceholder API

## Project Structure

```text
ass_2/
├── features/
│   ├── steps/
│   │   └── api_steps.py
│   ├── data_driven_api.feature
│   └── test_data.json
├── screenshots/
│   └── terminal_success.png
├── README.md
└── requirements.txt
```

## Implementation
The test data is loaded from the external JSON file using Python's JSON module.

For each post_id, a GET request is sent to:

```
https://jsonplaceholder.typicode.com/posts/<post_id>
```

The response status code is validated to ensure it is 200.

The returned post ID is also validated.

## Execution
Open PowerShell in the ass_2 directory and run:

```text
behave --no-capture
```

## Expected Result
All test data values should be processed successfully and all API responses should return status code 200.

## Actual Result
The test executed successfully for all five post IDs.

Post ID: 1
Post ID: 2
Post ID: 3
Post ID: 4
Post ID: 5

Behave execution result:

1 feature passed
1 scenario passed
3 steps passed
0 failed

## Source Code

```python
api_steps.py
```

## Output

The API requests returned status code 200 for the test data.

## Result

The data-driven API automation was successfully implemented using Python Behave and external JSON test data.

## Observation

A single BDD scenario was used to execute API validation for multiple post IDs. The test data was maintained separately from the automation logic.

## Conclusion

Data-driven testing using Python Behave and JSON test data was successfully implemented. The approach allows the same test scenario to be executed with multiple sets of input data while keeping the test data separate from the step definitions.
