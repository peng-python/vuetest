from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import mixins,viewsets,status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from .serializers import UserRegSerializer, UserDetailSerializer

User = get_user_model()

# Create your views here.


class UserViewSet(CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = UserRegSerializer
    queryset = User.objects.all()
    # authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserDetailSerializer
        elif self.action == 'create':
            return UserRegSerializer

        return UserDetailSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict['token'] = jwt_encode_handler(payload)
        re_dict['name'] = user.name if user.name else user.username
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

    # def get_object(self):
    #     return self.request.user

    # def get_permissions(self):
    #     if self.action == "retrieve":
    #         return [permissions.IsAuthenticated()]
    #     elif self.action == "create":
    #         return []
    #
    #     return []