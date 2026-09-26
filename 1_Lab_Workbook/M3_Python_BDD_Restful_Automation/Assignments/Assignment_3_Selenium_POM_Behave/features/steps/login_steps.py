# connects Gherkin to Python.

from behave import given, when, then

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage


@given("I open the automation practice website")
def step_open_website(context):

    context.driver = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()
        )
    )

    context.driver.maximize_window()

    context.driver.get(
        "https://testautomationpractice.blogspot.com/"
    )

    context.login_page = LoginPage(context.driver)

    print("\nAutomation Practice website opened")



@when("I enter my name through the POM")
def step_enter_name(context):

    context.login_page.enter_name("Arpan Mukherjee")

    print("Name entered through POM")


@when("I enter my email through the POM")
def step_enter_email(context):

    context.login_page.enter_email(
        "arpan@example.com"
    )

    print("Email entered through POM")


@when("I enter my phone number through the POM")
def step_enter_phone(context):

    context.login_page.enter_phone(
        "6294550814"
    )

    print("Phone number entered through POM")


@when("I select male gender through the POM")
def step_select_gender(context):

    context.login_page.select_male_gender()

    print("Male gender selected through POM")




@then("the form details should be displayed correctly")
def step_validate_form(context):

    assert context.login_page.get_name() == "Arpan Mukherjee"

    assert context.login_page.get_email() == (
        "arpan@example.com"
    )

    assert context.login_page.get_phone() == (
        "6294550814"
    )

    assert context.login_page.is_male_selected()

    print("Form validation passed")

    context.driver.save_screenshot(
        "screenshots/assignment_3_success.png"
    )

    context.driver.quit()

    print("Browser closed")
