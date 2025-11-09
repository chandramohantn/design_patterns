"""
Create different "views" of the context through interfaces, so each component only sees what it needs. 
"""


from abc import ABC, abstractmethod
from typing import Protocol


# Define focussed interfaces
class ReadOnlyContext(Protocol):
    """
    Read-only, safe data for general use.
    """
    @property
    def user_id(self) -> str:
        ...

    @property
    def tenant_id(self) -> str:
        ...

    @property
    def language(self) -> str:
        ...

class PaymentContext(Protocol):
    """
    Only payment-related data for payment services.
    """
    @property
    def payment_token(self) -> str:
        ...

    @property
    def api_key(self) -> str:
        ...

class DatabaseContext(Protocol):
    """
    Only database-related data for database services.
    """
    @property
    def database_password(self) -> str:
        ...

    @property
    def internal_service_url(self) -> str:
        ...