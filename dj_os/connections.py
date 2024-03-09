from django.conf import settings
from opensearchpy import OpenSearch


def get_client():
    return OpenSearch(settings.OPENSEARCH_HOSTS)
