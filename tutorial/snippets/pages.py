from rest_framework.pagination import PageNumberPagination


class DefaultPagination(PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    # 디폴트 페이지 사이즈
    page_size = 2
    # 해당 사이즈를 넘어갈 수 없음.
    max_page_size = 3
