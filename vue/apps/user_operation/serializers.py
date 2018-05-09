from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from goods.serializers import GoodsSerializer
from .models import UserFav, UserAddress ,UserLeavingMessage


class UserFavDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = UserFav
        fields = ('goods', 'id')


class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserFav
        validators = [UniqueTogetherValidator(
            queryset=UserFav.objects.all(),
            fields=('user', 'goods'),
            message='已经收藏'
        )] #验证是否收藏
        fields = ('user', 'goods', 'id')


class AddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserAddress
        fields = ('id', 'user', 'province', 'city', 'district', 'address', 'signer_name', 'signer_mobile', 'add_time')


class LeavingMessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserLeavingMessage
        fields = ('user', 'message_type', 'subject', 'message', 'file', 'add_time', 'id')
