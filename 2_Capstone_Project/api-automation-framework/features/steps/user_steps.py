import uuid
import jsonschema
from behave import given, when, then

from src.schemas.user_schemas import (
    BASIC_MESSAGE_SCHEMA,
    USER_DETAIL_SCHEMA,
    JSONPLACEHOLDER_USER_SCHEMA,
)


def _unique_email():
    return f"qa_user_{uuid.uuid4().hex[:10]}@example.com"


# ---------------------------------------------------------------------------
# Happy-path lifecycle: create -> verify login -> get -> update -> delete
# ---------------------------------------------------------------------------

@given("I have a new user's registration details")
def step_prepare_registration_details(context):
    context.request_payload = {
        "name": "QA Automation",
        "email": _unique_email(),
        "password": "P@ssw0rd123",
        "title": "Mr",
        "birth_date": "15",
        "birth_month": "6",
        "birth_year": "1995",
        "firstname": "QA",
        "lastname": "Automation",
        "company": "TestCorp",
        "address1": "123 Test Street",
        "address2": "",
        "country": "India",
        "zipcode": "700001",
        "state": "West Bengal",
        "city": "Kolkata",
        "mobile_number": "9999999999",
    }


@when("I create the user account")
def step_create_account(context):
    context.response = context.user_client.create_account(context.request_payload)
    context.created_user = context.request_payload


@then("the account should be created successfully")
def step_assert_account_created(context):
    body = context.response.json()
    jsonschema.validate(body, BASIC_MESSAGE_SCHEMA)
    assert body["responseCode"] == 201, f"Expected 201, got {body['responseCode']}: {body}"
    assert body["message"] == "User created!"


@when("I verify login with the created user's credentials")
def step_verify_login_valid(context):
    context.response = context.user_client.verify_login(
        email=context.created_user["email"],
        password=context.created_user["password"],
    )


@then("the login should be verified successfully")
def step_assert_login_verified(context):
    body = context.response.json()
    jsonschema.validate(body, BASIC_MESSAGE_SCHEMA)
    assert body["responseCode"] == 200
    assert body["message"] == "User exists!"


@when("I fetch the user detail by email")
def step_get_user_detail(context):
    context.response = context.user_client.get_user_by_email(context.created_user["email"])


@then("the returned user detail should match the created user")
def step_assert_user_detail(context):
    body = context.response.json()
    jsonschema.validate(body, USER_DETAIL_SCHEMA)
    assert body["user"]["email"] == context.created_user["email"]
    assert body["user"]["first_name"] == context.created_user["firstname"]


@when("I update the user's account information")
def step_update_account(context):
    updated_payload = dict(context.created_user)
    updated_payload["firstname"] = "QAUpdated"
    updated_payload["city"] = "Bengaluru"
    context.response = context.user_client.update_account(updated_payload)
    context.created_user = updated_payload


@then("the account should be updated successfully")
def step_assert_account_updated(context):
    body = context.response.json()
    jsonschema.validate(body, BASIC_MESSAGE_SCHEMA)
    assert body["responseCode"] == 200
    assert body["message"] == "User updated!"


@when("I delete the user's account")
def step_delete_account(context):
    context.response = context.user_client.delete_account(
        email=context.created_user["email"],
        password=context.created_user["password"],
    )


@then("the account should be deleted successfully")
def step_assert_account_deleted(context):
    body = context.response.json()
    jsonschema.validate(body, BASIC_MESSAGE_SCHEMA)
    assert body["responseCode"] == 200
    assert body["message"] == "Account deleted!"


# ---------------------------------------------------------------------------
# Negative scenarios
# ---------------------------------------------------------------------------

@given('the login request is missing the "{missing_field}" field')
def step_prepare_incomplete_login(context, missing_field):
    credentials = {"email": "someone@example.com", "password": "somepassword"}
    credentials.pop(missing_field, None)
    context.login_credentials = credentials


@given("a set of credentials that do not belong to any registered user")
def step_prepare_invalid_credentials(context):
    context.login_credentials = {
        "email": f"no_such_user_{uuid.uuid4().hex[:8]}@example.com",
        "password": "wrong-password",
    }


@when("I send the verify login request")
def step_send_login_request(context):
    context.response = context.user_client.verify_login(**context.login_credentials)


@then("the response code should be {expected_code:d}")
def step_assert_response_code(context, expected_code):
    body = context.response.json()
    assert body["responseCode"] == expected_code, (
        f"Expected {expected_code}, got {body['responseCode']}: {body}"
    )


@then('the response message should be "{expected_message}"')
def step_assert_response_message(context, expected_message):
    body = context.response.json()
    assert body["message"] == expected_message, (
        f"Expected '{expected_message}', got '{body['message']}'"
    )


# ---------------------------------------------------------------------------
# Non-functional check: response time
# ---------------------------------------------------------------------------

@then("the response time should be below {max_ms:d} ms")
def step_assert_response_time(context, max_ms):
    actual = context.user_client.last_response_time_ms
    assert actual < max_ms, f"Response took {actual:.2f} ms, expected under {max_ms} ms"


# ---------------------------------------------------------------------------
# Reusability demo: same framework, second API
# ---------------------------------------------------------------------------

@when("I fetch user {user_id:d} from JSONPlaceholder")
def step_get_jsonplaceholder_user(context, user_id):
    context.response = context.jsonplaceholder_client.get_user(user_id)


@then("the JSONPlaceholder response should match the user schema")
def step_assert_jsonplaceholder_schema(context):
    body = context.response.json()
    jsonschema.validate(body, JSONPLACEHOLDER_USER_SCHEMA)
    assert context.response.status_code == 200
