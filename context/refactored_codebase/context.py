"""
Centralized context module for shared configurations and utilities.
"""

from dataclasses import dataclass, asdict
from typing import Dict, Any, Optional
import uuid
from datetime import datetime


@dataclass(frozen=True) # Immutable context data structure to prevent accidental modifications
class AnalyticsContext:
    # User Context
    user_id: str
    user_tier: str = "standard"  # Default user tier

    # Tenant Context
    tenant_id: str
    tenant_region: str = "US"  # Default region

    # Session Context
    session_id: str = None
    device_type: str = "desktop"  # Default device type

    # Localization Context
    country: str = "US"  # Default country
    language: str = "en"  # Default language
    timezone: str = "UTC"  # Default timezone

    # Request Context
    request_id: str = None
    source_platform: str = "web"  # Default platform
    api_version: str = "v1"  # Default API version
    timestamp: str = None

    def __post_init__(self):
        # Generate unique session_id if not provided
        if self.session_id is None:
            object.__setattr__(self, 'session_id', str(uuid.uuid4()))
        
        # Generate unique request_id if not provided
        if self.request_id is None:
            object.__setattr__(self, 'request_id', str(uuid.uuid4()))
        
        # Set current timestamp if not provided
        if self.timestamp is None:
            object.__setattr__(self, 'timestamp', datetime.now(datetime.timezone.utc))

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the context dataclass to a dictionary for logging/storage.
        """
        return asdict(self)
    
    def with_additional_data(self, **kwargs) -> 'AnalyticsContext':
        """
        Create a new AnalyticsContext with additional data (immutable).
        """
        context_dict = self.to_dict()
        context_dict.update(kwargs)
        return AnalyticsContext(**context_dict)


