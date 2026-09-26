"""
JSON Schemas used to validate response STRUCTURE, not just status codes.

Checking `response.status_code == 200` only tells you the server didn't
error out - it says nothing about whether the fields you depend on are the
right shape. These schemas are the "contract" the API is expected to honor.
"""

BASIC_MESSAGE_SCHEMA = {
    "type": "object",
    "required": ["responseCode", "message"],
    "properties": {
        "responseCode": {"type": "integer"},
        "message": {"type": "string"},
    },
}

USER_DETAIL_SCHEMA = {
    "type": "object",
    "required": ["responseCode", "user"],
    "properties": {
        "responseCode": {"type": "integer"},
        "user": {
            "type": "object",
            "required": ["email", "first_name", "last_name"],
            "properties": {
                "email": {"type": "string"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
            },
        },
    },
}

JSONPLACEHOLDER_USER_SCHEMA = {
    "type": "object",
    "required": ["id", "name", "email", "username"],
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "username": {"type": "string"},
    },
}
