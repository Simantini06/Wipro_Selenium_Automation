# Assignment 6 – Windows, Tabs & Iframes

## Module
M1 – Automation with Selenium

## Experiment Title
Windows, Tabs & Iframes Handling using Selenium Python

## Problem Statement

Automate browser interactions involving iframes, multiple browser tabs, and window handles using Selenium WebDriver.

The automation should demonstrate how to switch into an iframe, return to the main page, open a new browser tab, identify multiple window handles, switch between tabs, close a child tab, and return to the original window.

## Objective

- To understand iframe handling in Selenium.
- To switch between the main page and an iframe.
- To open and handle a new browser tab.
- To retrieve browser window handles using `window_handles`.
- To switch between different browser windows/tabs.
- To close a child tab and return to the main window.

## Website Used

For the iframe portion:

https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe

For the new tab demonstration:

https://www.google.com

### Website Adaptation

The initially used Test Automation Practice website currently contains no iframe elements on the tested page.

Therefore, W3Schools Tryit Editor was used for the iframe portion of this experiment so that iframe handling could be demonstrated correctly.

## Tools and Technologies

- Python
- Selenium WebDriver
- Chrome Browser
- ChromeDriver
- WebDriver Manager
- XPath
- Browser Window Handles
- Iframes

## Implementation

### 1. Open the webpage

The W3Schools Tryit Editor page is opened using Selenium WebDriver.

### 2. Handle iframe

The iframe is located using XPath:

```python
iframe = driver.find_element(
    By.XPATH,
    "//iframe[@id='iframeResult']"
)
```

Selenium switches into the iframe using:

```python
driver.switch_to.frame(iframe)
```

After completing the iframe operation, Selenium switches back to the main page using:

```python
driver.switch_to.default_content()
```

### 3. Open a new tab

A new browser tab is opened using:

```python
driver.switch_to.new_window("tab")
```

Google is then opened in the new tab.

### 4. Get window handles

All currently open browser windows/tabs are retrieved using:

```python
handles = driver.window_handles
```

The handles are printed using a loop.

### 5. Switch between windows

The original window is selected using:

```python
driver.switch_to.window(handles[0])
```

The new tab is selected using:

```python
driver.switch_to.window(handles[1])
```

### 6. Close the child tab

After switching to the new tab, it is closed using:

```python
driver.close()
```

Selenium then switches back to the original window.

## Source Code

The complete Selenium implementation is available in:
```assignment6.py```

## Output

The program successfully produced output similar to:

Main page title: W3Schools Tryit Editor
Main window: <main_window_handle>

Switched to iframe successfully
Switched back to main page

New tab opened
New tab title: Google
New tab handle: <new_tab_handle>

Total windows/tabs: 2
Window handle: <main_window_handle>
Window handle: <new_tab_handle>

Switched back to main window
Main window title: W3Schools Tryit Editor

Switched to new tab
New tab closed
Returned to main window
Final window title: W3Schools Tryit Editor

## Result

The experiment was successfully completed.
Selenium WebDriver was used to:

1. Switch into an iframe.
2. Return to the main page.
3. Open a new browser tab.
4. Retrieve multiple window handles.
5. Switch between browser tabs.
6. Close the child tab.
7. Return to the original browser window.

## Observation

1. switch_to.frame() is used to interact with elements inside an iframe.
2. switch_to.default_content() returns Selenium to the main webpage.
3. window_handles returns the handles of all currently open browser windows/tabs.
4. switch_to.window() allows Selenium to move control between windows or tabs.
5. driver.close() closes the currently active browser tab/window.
6. driver.quit() closes the entire browser session.

## Conclusion

This experiment provided practical knowledge of handling iframes and multiple browser windows/tabs using Selenium WebDriver. These techniques are useful when automating modern web applications containing embedded content and multi-tab workflows.
