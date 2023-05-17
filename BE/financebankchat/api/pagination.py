# Create your views here.
# api/views.py
from rest_framework import pagination


class ExtraLargeResultsSetPagination(pagination.PageNumberPagination):
    """paginator for large data set
    """
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class LargeResultsSetPagination(pagination.PageNumberPagination):
    """paginator for large data set
    """
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 500


class MediumResultsSetPagination(pagination.PageNumberPagination):
    """paginator for large data set
    """
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 100
