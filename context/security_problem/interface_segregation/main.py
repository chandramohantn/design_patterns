"""
Main module for demonstrating the Interface Segregation Principle.
Compile-time security - Type checkers prevent accessing unauthorized data.
Explicit Dependencies - Functions declare exactly what they need.
Lazy Loading - Sensitive data is only loaded when accessed.
No Accidental Leaks - Impossible to accidentally log sensitive data.
"""

from base import ReadOnlyContext, PaymentContext, DatabaseContext
from secure_context import SecureContext


def log_user_action(context: ReadOnlyContext):
    # This logging function only has access to safe data
    # This function cannot access sensitive information even if it tries
    print(f"Logging action for user {context.user_id}")
    # context.api_key  # This would raise an error if uncommented

def process_payment(context: PaymentContext):
    # Payment service function that only has access to payment-related data
    print(f"Processing payment with token {context.payment_token}")
    result = payment_gateway.charge(context.payment_token, context.api_key)
    # context.database_password  # This would raise an error if uncommented
    return result

def setup_database(context: DatabaseContext):
    # Database setup function that only has access to database-related data
    print(f"Setting up database with URL {context.internal_service_url}")
    connection = connect(context.internal_service_url, context.database_password)
    # context.user_id  # This would raise an error if uncommented
    return connection


def main():
    # Create a secure context with all necessary data
    context = SecureContext(
        user_id="user123", 
        tenant_id="tenant456", 
        language="en"
    )

    # Each function gets only the context interface it needs
    log_user_action(context)  # ReadOnlyContext
    process_payment(context)  # PaymentContext
    setup_database(context)   # DatabaseContext
