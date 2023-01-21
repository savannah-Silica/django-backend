from rest_framework import pagination
class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 5
    page_query_param = 'page'
    page_size_query_param = 'per_page'
    max_page_size = 1000