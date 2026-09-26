"""
Wraps the "User Management" endpoints of https://automationexercise.com/api

Note: this API always replies with HTTP 200 at the transport level, but embeds
the real result in a `responseCode` field inside the JSON body (200/201/400/404).
Step definitions assert on `responseCode`, not `response.status_code`, for that
reason - this is a well-known quirk of this particular API.

Also note: these endpoints expect form-encoded data, not JSON, hence `data=`
instead of `json=` in every call.
"""

from src.clients.base_client import BaseAPIClient


class UserClient(BaseAPIClient):
    def create_account(self, payload):
        return self.post("createAccount", data=payload)

    def verify_login(self, email=None, password=None):
        payload = {}
        if email is not None:
            payload["email"] = email
        if password is not None:
            payload["password"] = password
        return self.post("verifyLogin", data=payload)

    def update_account(self, payload):
        return self.put("updateAccount", data=payload)

    def delete_account(self, email, password):
        return self.delete("deleteAccount", data={"email": email, "password": password})

    def get_user_by_email(self, email):
        return self.get("getUserDetailByEmail", params={"email": email})
