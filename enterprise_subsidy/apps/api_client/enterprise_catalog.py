"""
Enterprise Catalog api client for the subsidy service.
"""
import logging
from urllib.parse import urljoin

import requests
from django.conf import settings

from enterprise_subsidy.apps.api_client.base_oauth import BaseOAuthClient

logger = logging.getLogger(__name__)


class EnterpriseCatalogApiClient(BaseOAuthClient):
    """
    API client for calls to the enterprise service.
    """
    api_base_url = urljoin(settings.ENTERPRISE_CATALOG_URL, 'api/v1/')
    enterprise_customer_endpoint = urljoin(api_base_url, 'enterprise-customer/')

    def enterprise_customer_url(self, enterprise_customer_uuid):
        return urljoin(
            self.enterprise_customer_endpoint,
            f"{enterprise_customer_uuid}/",
        )

    def content_metadata_url(self, enterprise_customer_uuid, content_identifier):
        return urljoin(
            self.enterprise_customer_url(enterprise_customer_uuid),
            f'content-metadata/{content_identifier}/'
        )

    def get_content_metadata_for_customer(self, enterprise_customer_uuid, content_identifier):
        """
        Returns Enterprise Customer related data for a specified piece on content.

        Arguments:
            enterprise_customer_uuid (UUID): UUID of the customer associated with an enterprise
            content_identifier (str): **Either** the content UUID or content key identifier for a content record.
                Note: the content needs to be owned by a catalog associated with the provided customer else this
                method will throw an HTTPError.
        Returns:
            response (dict): JSON response object associated with a content metadata record
        Raises:
            requests.exceptions.HTTPError: if service is down/unavailable or status code comes back >= 300,
            the method will log and throw an HTTPError exception. A 404 exception will be thrown if the content
            does not exist, or is not present in a catalog associated with the customer.
        """
        content_metadata_url = self.content_metadata_url(enterprise_customer_uuid, content_identifier)
        try:
            response = self.client.get(content_metadata_url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as exc:
            if hasattr(response, 'text'):
                logger.error(
                    f'Failed to fetch enterprise customer data for {enterprise_customer_uuid} because {response.text}',
                )
            raise exc
