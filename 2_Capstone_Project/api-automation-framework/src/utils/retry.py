"""
Small dependency-free retry decorator for HTTP calls.

Retries on:
  - connection errors / timeouts (the request never got a response)
  - configurable server-side status codes (default: 500, 502, 503, 504)

Does NOT retry on 4xx codes, since those are usually deterministic
(bad request, not found, etc.) and retrying them would just waste time.
"""

import time
import functools
import requests


def retry_on_failure(max_attempts=3, backoff_seconds=1, retry_on_status=(500, 502, 503, 504)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None

            for attempt in range(1, max_attempts + 1):
                try:
                    response = func(*args, **kwargs)
                    if response.status_code in retry_on_status and attempt < max_attempts:
                        time.sleep(backoff_seconds * attempt)
                        continue
                    return response
                except (requests.ConnectionError, requests.Timeout) as exc:
                    last_exception = exc
                    if attempt < max_attempts:
                        time.sleep(backoff_seconds * attempt)
                        continue

            raise last_exception

        return wrapper

    return decorator
