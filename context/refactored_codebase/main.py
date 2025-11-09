"""
Main module to demonstrate the usage of AnalyticsService with refactored parameters.
"""

from analytics_service import AnalyticsService
from context import AnalyticsContext


def main():
    service = AnalyticsService()

    # Create a context object to encapsulate all parameters
    context = AnalyticsContext(
        user_id="user123",
        tenant_id="tenant456",
        session_id="session789",
        device_type="mobile",
        country="US",
        language="en",
        user_tier="premium",
        timestamp="2024-01-15T10:30:00Z",
        source_platform="web",
        api_version="v2"
    )

    # Pass the context object to the service method
    service.track_user_behavior(
        context,
        event_type="purchase",
        event_data={"product_id": "prod1", "amount": 99.99}
    )

    service.track_user_behavior(
        context,
        event_type="page_view",
        event_data={"page_url": "/home"}
    )

    # Can easily create variations
    eu_context = context.with_additional_data(country="DE", language="de", tenant_region="EU")
    service.track_user_behavior(
        eu_context,
        event_type="purchase",
        event_data={"product_id": "prod2", "amount": 149.99}
    )

if __name__ == "__main__":
    main()
