"""
Support service module - now with clean interfaces.
"""

from context import AnalyticsContext
from typing import Dict

class AccessService:
    def check_analytics_access(self, context: AnalyticsContext) -> bool:
        """
        Can access any context field as needed.
        """
        print(f"Checking access for user {context.user_id} in tenant {context.tenant_id}")
        return context.user_tier in ["premium", "enterprise"]

class EnrichmentService:
    def enrich(self, context: AnalyticsContext, event_data: dict, event_type: str) -> dict:
        """
        Enrich event data using context.
        """
        enriched = {
            **event_data,
            "context": {
                "user_tier": context.user_tier,
                "country": context.country,
                "language": context.language,
                "device_type": context.device_type,
                "platform": context.source_platform
            },
            "metadata": {
                "request_id": context.request_id,
                "tenant_id": context.tenant_id,
                "timestamp": context.timestamp
            }
        }
        print(f"Enriched event with context for {context.user_id}")
        return enriched
    
class ProcessingService:
    def process(self, context: AnalyticsContext, enriched_data: dict) -> dict:
        """
        Process enriched data based on tenant-specific rules.
        """
        print(f"Processing data for tenant {context.tenant_id} in region {context.tenant_region}")
        if context.tenant_region == "EU":
            enriched_data = self._apply_gdpr_rules(context, enriched_data)
        
        print(f"Processed event for tenant {context.tenant_id} in {context.tenant_region}")
        return enriched_data
    
    def _apply_gdpr_rules(self, context: AnalyticsContext, data: Dict) -> Dict:
        """
        GDPR logic with context available
        """
        if context.country in ["DE", "FR", "IT"]:
            data = {**data, "gdpr_compliant": True}
        return data

class StorageService:
    def store_event(self, context: AnalyticsContext, processed_data: Dict):
        """
        Storage with full context for partitioning/archiving
        """
        storage_key = f"events/{context.tenant_id}/{context.user_id}/{context.timestamp}"
        print(f"Storing event at {storage_key}")

class MetricsService:
    def update_metrics(self, context: AnalyticsContext, event_type: str, processed_data: Dict):
        """
        Metrics with dimensional context
        """
        dimensions = {
            "tenant": context.tenant_id,
            "user_tier": context.user_tier,
            "country": context.country,
            "device_type": context.device_type,
            "platform": context.source_platform
        }
        print(f"Updating metrics for {event_type} with dimensions: {dimensions}")
