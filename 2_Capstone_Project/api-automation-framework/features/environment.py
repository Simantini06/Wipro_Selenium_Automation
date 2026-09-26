"""
Behave lifecycle hooks.

- before_all: reads config.yaml (respecting `behave -D env=<name>`) and builds
  the API clients that step definitions will use.
- before_scenario: resets per-scenario state.
- after_step: attaches the request/response of whatever call just happened
  to the Allure report, so a failed test shows exactly what was sent and
  received instead of just a red X.
"""

import os
import sys
import json

# Make sure `src` is importable regardless of the working directory behave
# was launched from.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import allure  # noqa: E402

from src.config_reader import ConfigReader  # noqa: E402
from src.clients.user_client import UserClient  # noqa: E402
from src.clients.jsonplaceholder_client import JSONPlaceholderUserClient  # noqa: E402


def before_all(context):
    env_name = context.config.userdata.get("env")
    env_config = ConfigReader.get_environment(env_name)

    context.env_config = env_config
    context.user_client = UserClient(
        base_url=env_config["base_url"],
        timeout=env_config.get("timeout", 15),
    )

    # Used only by features/reusability_demo.feature to prove the same
    # framework works against a second, unrelated API.
    jp_config = ConfigReader.get_environment("jsonplaceholder")
    context.jsonplaceholder_client = JSONPlaceholderUserClient(
        base_url=jp_config["base_url"],
        timeout=jp_config.get("timeout", 15),
    )


def before_scenario(context, scenario):
    context.response = None
    context.request_payload = None
    context.created_user = None
    context.login_credentials = None


def after_step(context, step):
    for attr_name, label in (
        ("user_client", "Primary API"),
        ("jsonplaceholder_client", "JSONPlaceholder API"),
    ):
        client = getattr(context, attr_name, None)
        if client is None or client.last_response is None:
            continue

        _attach_api_call_log(client, step, label)
        # Prevent the same call from being re-attached to unrelated later steps.
        client.last_response = None


def _attach_api_call_log(client, step, label):
    request_info = client.last_request or {}
    response = client.last_response

    try:
        response_body = json.dumps(response.json(), indent=2)
    except ValueError:
        response_body = response.text

    log_text = (
        f"Request:\n"
        f"  Method : {request_info.get('method')}\n"
        f"  URL    : {request_info.get('url')}\n"
        f"  Params : {request_info.get('params')}\n"
        f"  Data   : {request_info.get('data')}\n\n"
        f"Response:\n"
        f"  Status Code   : {response.status_code}\n"
        f"  Time Taken    : {client.last_response_time_ms:.2f} ms\n"
        f"  Body          :\n{response_body}"
    )

    allure.attach(
        log_text,
        name=f"{label} - {step.name}",
        attachment_type=allure.attachment_type.TEXT,
    )
