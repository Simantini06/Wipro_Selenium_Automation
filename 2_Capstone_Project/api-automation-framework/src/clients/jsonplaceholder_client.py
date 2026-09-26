"""
Points the SAME BaseAPIClient at a completely different API.

This exists purely to prove the framework is reusable, not hardcoded around
one service: swap the base_url in config.yaml and everything (retries,
timing, Allure logging) keeps working unchanged.
"""

from src.clients.base_client import BaseAPIClient


class JSONPlaceholderUserClient(BaseAPIClient):
    def get_user(self, user_id):
        return self.get(f"users/{user_id}")

    def list_users(self):
        return self.get("users")

    def create_user(self, payload):
        return self.post("users", json=payload)
