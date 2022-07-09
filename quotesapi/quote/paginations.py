from rest_framework.pagination import PageNumberPagination

class BigSetPagination(PageNumberPagination):
    page_size = 30