"""
Support views for security problem context.
"""

from secure_context import SecureContext


class PublicContextView:
    """
    Safe for logging, UI, general business logic.
    """
    def __init__(self, context: SecureContext):
        self._context = context

    @property
    def user_id(self) -> str:
        return self._context._user_id
    
    @property
    def tenant_id(self) -> str:
        return self._context._tenant_id
    
    @property
    def language(self) -> str:
        return self._context._language
    
    def to_log_dict(self) -> dict:
        """
        Safe for logging - no sensitive data
        """
        return {
            "user_id": self.user_id,
            "tenant_id": self.tenant_id,
            "language": self.language
        }
    
class PaymentContextView:
    """
    Only for payment services
    """
    def __init__(self, context: SecureContext):
        self._context = context

    @property
    def user_id(self) -> str:
        return self._context._user_id
    
    @property
    def payment_token(self) -> str:
        return self._context._get_payment_token()
    

class DatabaseContextView:
    """
    Only for database access
    """
    def __init__(self, context: SecureContext):
        self._context = context
    
    @property
    def database_password(self) -> str:
        return self._context._get_database_password()
    
    @property
    def internal_service_url(self) -> str:
        return self._context._get_internal_service_url()
    