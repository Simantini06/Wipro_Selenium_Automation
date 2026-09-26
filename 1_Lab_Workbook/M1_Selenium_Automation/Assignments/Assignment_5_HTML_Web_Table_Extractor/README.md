# Assignment 5 – HTML Web Table Extractor

## Module Name

M1 – Automation with Selenium

## Experiment Title

HTML Web Table Extractor

## Problem Statement

Automate the extraction of data from an HTML web table using Selenium WebDriver.

The task is to:
- Identify the web table.
- Iterate through its rows and columns.
- Extract and display the table data.
- Find a particular book by its name.
- Retrieve the corresponding price.

## Objective

To learn how to:
- Locate HTML tables using XPath.
- Find table rows and columns using Selenium.
- Iterate through WebElements.
- Extract text from table cells.
- Search for a specific row.
- Retrieve data from a particular column.

## Website Used

Test Automation Practice

URL:
https://testautomationpractice.blogspot.com/

## Tools and Technologies

- Python
- Selenium WebDriver
- Chrome Browser
- WebDriver Manager
- XPath
- HTML Tables

## Implementation

### Step 1 – Open the Website

The Test Automation Practice website is opened using Selenium WebDriver.

### Step 2 – Locate the Table

The table is located using XPath:
```python
//table[@name='BookTable']/tbody/tr
```

### 3 – Find Table Rows

The find_elements() method is used to retrieve all table rows.
```python
rows = driver.find_elements(
    By.XPATH,
    "//table[@name='BookTable']/tbody/tr"
)
```

The script identifies 7 rows, including the header row.

### 4 – Extract Table Data

Each row is processed using:
```python
columns = row.find_elements(By.TAG_NAME, "td")
```
The text from each cell is then displayed.

### 5 – Find a Particular Book

The script searches for:
Master In Selenium

The book name is compared with the first column of each row.

### 6 – Retrieve the Price

The price is retrieved from the fourth column:
columns[3].text

The retrieved price is:
3000

## Source Code

The complete implementation is available in:
```assignment5.py```

## Output

The program successfully extracted the table data and retrieved the price of the selected book.

Terminal Output
Total rows: 7
Book Details
--------------------------------------------------
Learn Selenium | Amit | Selenium | 300 |
Learn Java | Mukesh | Java | 500 |
Learn JS | Animesh | Javascript | 300 |
Master In Selenium | Mukesh | Selenium | 3000 |
Master In Java | Amod | JAVA | 2000 |
Master In JS | Amit | Javascript | 1000 |
--------------------------------------------------
Book: Master In Selenium
Price: 3000

## Result

The HTML web table was successfully located and its rows and columns were extracted using Selenium WebDriver.
The required book, Master In Selenium, was successfully located and its price, 3000, was retrieved.

## Observation

1. Selenium can locate HTML table elements using XPath.
2. find_elements() can be used to retrieve multiple table rows.
3. find_elements(By.TAG_NAME, "td") retrieves cells within a row.
4. Table data can be processed using Python loops.
5. Searching within an individual row makes it possible to retrieve related information such as price.

## Conclusion

The experiment successfully demonstrated HTML web table extraction using Selenium with Python. The table was traversed row by row and column by column, and specific information was retrieved from the required row.
