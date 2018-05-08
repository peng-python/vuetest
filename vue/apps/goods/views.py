from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.pagination import PageNumberPagination

from .serializers import CategorySerializer, GoodsSerializer
from .models import  GoodsModel, GoodsCategory

# Create your views here.


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class GoodsPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class GoodsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = GoodsModel.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination