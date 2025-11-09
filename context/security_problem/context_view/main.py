"""
Main module for the security problem context view.
Runtime Security - Views physically dont have sensitive data methods
Clear Intent - The view type documents what data a function needs
No Type System Dependency - Works without type checking
Explicit Data Flow - You have to consciously choose which view to create
"""

from logging import getLogger
logger = getLogger(__name__)
from support_views import PublicContextView, PaymentContextView, DatabaseContextView
from secure_context import SecureContext


def log_user_action(context: PublicContextView):
    # Can only access public data
    print(f"User {context.user_id} performed action")
    safe_data = context.to_log_dict()
    logger.info(safe_data)  # No risk of leaking secrets!
    
    # These would cause AttributeError:
    # context.payment_token  # ← No such attribute!
    # context.database_password  # ← No such attribute!

def process_payment(context: PaymentContextView):
    # Can access payment token
    print(f"Processing payment for user {context.user_id} with token {context.payment_token}")
    result = payment_gateway.charge(context.user_id, context.payment_token)
    # These would cause AttributeError:
    # context.database_password  # ← No such attribute!

def setup_database_connection(context: DatabaseContextView):
    # Can access database password
    print(f"Setting up DB connection with password {context.database_password}")
    connect(url=context._context._internal_service_url, password=context.database_password)
    # These would cause AttributeError:
    # context.payment_token  # ← No such attribute!

def handle_user_request(secure_context: SecureContext):
    # Different parts of the code get only the views they need
    public_view = secure_context.get_public_data()
    log_user_action(public_view)

    payment_view = secure_context.get_payment_data()
    process_payment(payment_view)

    db_view = secure_context.get_database_data()
    setup_database_connection(db_view)

    # Security: Cannot accidentally pass wrong view
    log_user_action(payment_view)  # ← This would raise an error!
