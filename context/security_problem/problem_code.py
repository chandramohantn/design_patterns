"""
This module demonstrates a security problem where a single context object
contains both public and sensitive information, leading to potential data leaks.
When every method gets the full context, you violate the principle of least privilege - code should only have access to the data it needs.
"""

from dataclasses import dataclass


@dataclass
class GodContext:
    # Public data (safe for everyone)
    user_id: str
    tenant_id: str
    language: str

    # Private data (sensitive information)
    api_key: str = "secret_api_key"
    database_password: str = "super_secret_password"
    payment_token: str = "sensitive_payment_token"
    internal_service_url: str = "http://internal.service.local"

# Now every function that needs context will receive a GodContext object,
# which contains both public and private data, leading to potential security risks.
def log_user_action(context: GodContext):
    # This logging function inadvertently exposes sensitive information
    print(f"Logging action for user {context.user_id} with API key {context.api_key}")
    # In a real application, this could lead to sensitive data being logged or exposed.

def render_ui(context: GodContext):
    # UI rendering function that has access to sensitive data it doesn't need
    print(f"Rendering UI for user {context.user_id} in language {context.language}")
    # The function has access to context.api_key, context.database_password, etc.,
    # which it does not need, increasing the risk of accidental exposure.

def call_payment_service(context: GodContext):
    # Payment service function that uses sensitive payment token
    print(f"Calling payment service for user {context.user_id} with token {context.payment_token}")
 
