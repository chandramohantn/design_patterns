"""
Main context with all data (but properly secured).
"""

from support_views import PublicContextView, PaymentContextView, DatabaseContextView


class SecureContext:
    def __init__(self, user_id: str, tenant_id: str, language: str):
        # Public data (safe for everyone)
        self._user_id = user_id
        self._tenant_id = tenant_id
        self._language = language
        self._sensitive_data = {}

    # Public methods - safe for anyone
    def get_public_data(self) -> 'PublicContextView':
        return PublicContextView(self)
    
    # Payment related methods - only for payment services
    def get_payment_data(self) -> 'PaymentContextView':
        return PaymentContextView(self)
    
    # Database related methods - only for database access
    def get_database_data(self) -> 'DatabaseContextView':
        return DatabaseContextView(self)
    
    # Internal methods to access sensitive data
    def _get_user_id(self) -> str:
        return self._user_id
    
    def _get_payment_token(self) -> str:
        if "payment_token" not in self._sensitive_data:
            self._sensitive_data["payment_token"] = self._load_payment_token()
        return self._sensitive_data.get("payment_token", "")
    
    def _get_database_password(self) -> str:
        if "database_password" not in self._sensitive_data:
            self._sensitive_data["database_password"] = self._load_database_password()
        return self._sensitive_data.get("database_password", "")
