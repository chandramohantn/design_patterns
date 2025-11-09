"""
Main module for the analytics service context.
"""

from analytics_service import AnalyticsService

service = AnalyticsService()

# 12 parameters! And this will keep growing
service.track_user_behavior(
    user_id="user123",
    tenant_id="tenant456", 
    session_id="session789",
    device_type="mobile",
    country="US",
    language="en",
    user_tier="premium",
    timestamp="2024-01-15T10:30:00Z",
    event_type="purchase",
    event_data={"product_id": "prod1", "amount": 99.99},
    source_platform="web",
    api_version="v2"
)