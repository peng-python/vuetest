from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .serializers import CategorySerializer, GoodsSerializer
from .models import  GoodsModel, GoodsCategory
from .filters import GoodsFilter

# Create your views here.


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class GoodsPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class GoodsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = GoodsModel.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc') # 搜索
    ordering_fields = ('sold_num', 'shop_price') # 排序

    def retrieve(self, request, *args, **kwargs): # 点击量
        instanece = self.get_object()
        instanece.click_num += 1
        instanece.save()
        serializer = self.get_serializer(instanece)
        return Response(serializer.data)