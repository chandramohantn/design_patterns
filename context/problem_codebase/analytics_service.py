"""
A service that processes user behavior analytics.
"""

from support_service import AccessService, EnrichmentService, ProcessingService, StorageService, MetricsService

class AnalyticsService:
    def track_user_behavior(self, user_id, tenant_id, session_data, device_type, country, language, user_tier, timestamp, event_type, event_data, source_platform, api_version):
        """
        Track user behavior across multi-tenant e-commerce platform.
        """
        print(f"Processing event for user {user_id} in tenant {tenant_id}")

        # Validate user access based on tenant and user tier
        if not self._validate_user_access(user_id, tenant_id, user_tier):
            print(f"User {user_id} does not have access to analytics in tenant {tenant_id}")
            return
        
        # Enrich event data with contextual information
        enriched_data = self._enrich_event_data(user_id, tenant_id, country, language, user_tier, event_type, event_data, source_platform)

        # Process based on tenant-specific rules
        processed_data = self._process_for_tenant(tenant_id, country, language, enriched_data, api_version)

        # Store the event data
        self._store_analytics_event(user_id, tenant_id, session_data, device_type, timestamp, processed_data)

        # Update real-time metrics
        self._update_real_time_metrics(tenant_id, event_type, country, user_tier, processed_data)

    def _validate_user_access(self, user_id, tenant_id, user_tier):
        """
        Validate if the user has access to analytics features based on tenant and user tier.
        """
        access_service = AccessService()
        return access_service.check_analytics_access(user_id, tenant_id, user_tier)
    
    def _enrich_event_data(self, user_id, tenant_id, country, language, user_tier, event_type, event_data, source_platform):
        """
        Enrich event data with additional contextual information.
        """
        enrichment_service = EnrichmentService()
        return enrichment_service.enrich(event_data, user_id, tenant_id, country, language, user_tier, event_type, source_platform)
    
    def _process_for_tenant(self, tenant_id, country, language, enriched_data, api_version):
        """
        Apply tenant-specific processing rules to the enriched event data.
        """
        processing_service = ProcessingService()
        return processing_service.process(tenant_id, country, language, enriched_data, api_version)
    
    def _store_analytics_event(self, user_id, tenant_id, session_data, device_type, timestamp, processed_data):
        """
        Store the processed analytics event in the database.
        """
        storage_service = StorageService()
        storage_service.store_event(user_id, tenant_id, session_data, device_type, timestamp, processed_data)

    def _update_real_time_metrics(self, tenant_id, event_type, country, user_tier, processed_data):
        """
        Update real-time analytics metrics based on the processed event data.
        """
        metrics_service = MetricsService()
        metrics_service.update_metrics(tenant_id, event_type, country, user_tier, processed_data)

