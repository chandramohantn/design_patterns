"""
Clean and refactored analytics service module.
"""

from context import AnalyticsContext
from support_service import AccessService, EnrichmentService, ProcessingService, StorageService, MetricsService


class AnalyticsService:
    def track_user_behavior(self, context: AnalyticsContext, event_type: str, event_data: dict):
        """
        Track user behavior across multi-tenant e-commerce platform.
        Clean method signature - Only 3 parameters.
        All contextual information is encapsulated in AnalyticsContext object.
        """
        print(f"Processing event for user {context.user_id} in tenant {context.tenant_id}")

        # Validate user access based on tenant and user tier
        if not self._validate_user_access(context):
            print(f"User {context.user_id} does not have access to analytics in tenant {context.tenant_id}")
            return
        
        # Enrich event data with contextual information
        enriched_data = self._enrich_event_data(context, event_type, event_data)

        # Process based on tenant-specific rules
        processed_data = self._process_for_tenant(context, enriched_data)

        # Store the event data
        self._store_analytics_event(context, processed_data)

        # Update real-time metrics
        self._update_realtime_metrics(context, event_type, processed_data)

    def _validate_user_access(self, context: AnalyticsContext) -> bool:
        """
        Validate if the user has access to analytics features based on tenant and user tier.
        """
        access_service = AccessService()
        return access_service.check_analytics_access(context)
    
    def _enrich_event_data(self, context: AnalyticsContext, event_type: str, event_data: dict) -> dict:
        """
        Enrich event data with additional contextual information.
        """
        enrichment_service = EnrichmentService()
        return enrichment_service.enrich(context, event_data, event_type)
    
    def _process_for_tenant(self, context: AnalyticsContext, enriched_data: dict) -> dict:
        """
        Apply tenant-specific processing rules to the enriched event data.
        """
        processing_service = ProcessingService()
        return processing_service.process(context, enriched_data)
    
    def _store_analytics_event(self, context: AnalyticsContext, processed_data: dict):
        """
        Store the processed analytics event in the database.
        """
        storage_service = StorageService()
        storage_service.store_event(context, processed_data)

    def _update_realtime_metrics(self, context: AnalyticsContext, event_type: str, processed_data: dict):
        """
        Update real-time analytics metrics based on the processed event data.
        """
        metrics_service = MetricsService()
        metrics_service.update_metrics(context, event_type, processed_data)
