from rest_framework.pagination import PageNumberPagination

class WatchListPagination(PageNumberPagination):
    """Defining a pagination"""
    page_size = 10
    