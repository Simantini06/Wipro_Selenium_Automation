# Assignment 3 – Dynamic Dropdowns & Checkboxes

## Module

**M1 – Automation with Selenium**

## Experiment Title

**Dynamic Dropdowns & Checkboxes**

---

## Problem Statement

Automate checkbox selection and a scrolling/dynamic dropdown using Selenium WebDriver.

The task is to:

1. Locate all checkboxes on the webpage.
2. Check whether each checkbox is already selected.
3. Select the unchecked checkboxes.
4. Verify the number of selected checkboxes.
5. Open the scrolling dropdown.
6. Locate the required dropdown item.
7. Select the required item using Selenium.

---

## Objective

The objective of this experiment is to understand and implement:

- `find_elements()` for locating multiple web elements.
- Checkbox handling using `is_selected()`.
- Selecting unchecked checkboxes using `click()`.
- Handling a scrolling/dynamic dropdown.
- Locating dropdown items using XPath.
- Iterating through elements using a `for` loop.
- Selecting a required dropdown option.

---

## Website Used

**Test Automation Practice**

https://testautomationpractice.blogspot.com/

---

## Tools & Technologies

- Python
- Selenium WebDriver
- Chrome Browser
- WebDriver Manager
- XPath
- Selenium WebElements
- `find_elements()`
- `is_selected()`
- `click()`
- `for` loop

---

## Implementation

1. Browser Setup
2. Open the Website
3. Locate All Checkboxes
4. Select Unchecked Checkboxes
5. Verify Selected Checkboxes
6. Handle the Scrolling Dropdown

 ## Source Code

The complete implementation is available in:
`assignment3.py`

## Output

The program displays the total number of checkboxes and the number of selected checkboxes in the terminal.

Example:

Total checkboxes: 12
Selected checkboxes: 12
Dropdown Selection

The required item is selected from the scrolling dropdown.

Example:

Selected Item 50

## Result

The checkbox and scrolling dropdown automation was successfully executed using Selenium WebDriver.
All unchecked checkboxes were selected and verified, and the required item was selected from the scrolling dropdown.

## Observation

1. find_elements() can be used to locate multiple elements at once.
2. is_selected() helps determine the current state of a checkbox.
3. A for loop can be used to process multiple web elements.
4. XPath can be used to locate specific dropdown items.
5. Selenium can automate scrolling/dynamic dropdown interactions.

## Conclusion

This experiment provided practical experience in handling checkboxes and dynamic/scrolling dropdowns using Selenium with Python.
The experiment successfully demonstrated element identification, state verification, iteration, and interaction with web elements.   
