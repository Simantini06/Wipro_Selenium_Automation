"""
Generic, reusable HTTP client.

Resource-specific clients (UserClient, JSONPlaceholderUserClient, ...) inherit
from this instead of calling `requests` directly. That means every request -
regardless of which API it targets - automatically gets:
  - a shared session (connection reuse, shared headers)
  - consistent timeout handling
  - automatic retries on transient failures
  - response-time measurement
  - the last request/response kept around for logging into Allure

This is the "API Object Model" layer: step definitions never touch `requests`
directly, they only ever call methods on a client.
"""

import time
import requests

from src.utils.retry import retry_on_failure


class BaseAPIClient:
    def __init__(self, base_url, timeout=15, default_headers=None):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        if default_headers:
            self.session.headers.update(default_headers)

        # Populated after every call - used for Allure attachments and
        # response-time assertions in step definitions.
        self.last_request = None
        self.last_response = None
        self.last_response_time_ms = None

    def _build_url(self, endpoint):
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    @retry_on_failure(max_attempts=3, backoff_seconds=1)
    def _send(self, method, endpoint, **kwargs):
        url = self._build_url(endpoint)
        kwargs.setdefault("timeout", self.timeout)

        self.last_request = {
            "method": method,
            "url": url,
            "params": kwargs.get("params"),
            "data": kwargs.get("data"),
            "json": kwargs.get("json"),
            "headers": dict(self.session.headers),
        }

        start = time.perf_counter()
        response = self.session.request(method, url, **kwargs)
        elapsed_ms = (time.perf_counter() - start) * 1000

        self.last_response = response
        self.last_response_time_ms = elapsed_ms
        return response

    def get(self, endpoint, **kwargs):
        return self._send("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self._send("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self._send("PUT", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._send("DELETE", endpoint, **kwargs)
