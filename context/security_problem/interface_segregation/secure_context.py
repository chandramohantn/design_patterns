"""
Implement a secure context that supports all interfaces.
"""

from base import ReadOnlyContext, PaymentContext, DatabaseContext

class SecureContext(ReadOnlyContext, PaymentContext, DatabaseContext):
    def __init__(
        self,
        user_id: str,
        tenant_id: str,
        language: str
    ):
        # Public data
        self._user_id = user_id
        self._tenant_id = tenant_id
        self._language = language

        # Private data - loaded only when needed
        self._payment_token = None
        self._api_key = None
        self._database_password = None
        self._internal_service_url = None

    @property
    def user_id(self) -> str:
        return self._user_id
    
    @property
    def tenant_id(self) -> str:
        return self._tenant_id
    
    @property
    def language(self) -> str:
        return self._language
    
    # PaymentContext implementation - with security controls
    @property
    def payment_token(self) -> str:
        if self._payment_token is None:
            # Lazy load - only fetch when actually needed
            self._payment_token = self._load_payment_token()
        return self._payment_token
    
    @property
    def api_key(self) -> str:
        if self._api_key is None:
            self._api_key = self._load_api_key()
        return self._api_key
    
    # DatabaseContext implementation - with security controls
    @property
    def database_password(self) -> str:
        if self._database_password is None:
            self._database_password = self._load_database_password()
        return self._database_password
    
    @property
    def internal_service_url(self) -> str:
        if self._internal_service_url is None:
            self._internal_service_url = self._load_internal_service_url()
        return self._internal_service_url
    
    # Private loading methods
    def _load_payment_token(self) -> str:
        # Simulate secure loading of payment token
        return "sensitive_payment_token"
    
    def _load_api_key(self) -> str:
        # Simulate secure loading of API key
        return "secret_api_key"
    
    def _load_database_password(self) -> str:
        # Simulate secure loading of database password
        return "super_secret_password"
    
    def _load_internal_service_url(self) -> str:
        # Simulate secure loading of internal service URL
        return "http://internal.service.local"
    
    