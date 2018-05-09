from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

from utils.permissions import IsOwnerOrReadOnly

from .models import UserFav, UserAddress, UserLeavingMessage
from .serializers import UserFavSerializer, UserFavDetailSerializer, AddressSerializer, LeavingMessageSerializer

# Create your views here.


class UserFavViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    lookup_field = 'goods_id' # 查找字段

    def get_queryset(self):# 返回当前用户
        return UserFav.objects.filter(user=self.request.user)

    # def get_serializer_class(self): # 判断是
    def get_serializer_class(self):
        if self.action == "list":
            return UserFavDetailSerializer
        elif self.action == "create":
            return UserFavSerializer

        return UserFavSerializer


class AddressViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = AddressSerializer

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)


class LeavingMessageViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = LeavingMessageSerializer

    def get_queryset(self):
        return UserLeavingMessage.objects.filter(user=self.request.user)