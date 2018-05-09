from rest_framework import serializers
import time

from goods.models import GoodsModel
from .models import ShopCart, OrderInfo, OrderDetail
from goods.serializers import GoodsSerializer


class ShopCartDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(many=False, read_only=True)

    class Meta:
        model = ShopCart
        fields = ('goods', 'nums')


class ShopCartSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    nums = serializers.IntegerField(required=True, label='数量', min_value=1,
                                    error_messages={
                                        'min_value':'商品数量不能小于一',
                                        'required':'请选择购买数量'
                                    })
    goods = serializers.PrimaryKeyRelatedField(required=True, queryset=GoodsModel.objects.all()) # 返回对应商品的主键

    def create(self, validated_data):
        """"
        获得对应的用户名，商品数量和对应的商品
        """
        user = self.context['request'].user
        nums = validated_data['nums']
        goods = validated_data['goods']

        existed = ShopCart.objects.filter(user=user, goods=goods) # 查询该用户对应的该商品是否在购物车中

        if existed:
            existed = existed[0]
            existed.nums += nums
            existed.save()
        else:
            existed = ShopCart.objects.create(**validated_data) # 创建购物车

        return existed

    def update(self, instance, validated_data):
        instance.nums = validated_data['nums']
        instance.save()
        return instance


class OrderGoodsSerializer(serializers.ModelSerializer): # 订单的商品详情
    goods = GoodsSerializer(many=False)

    class Meta:
        model = OrderDetail
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    goods = OrderGoodsSerializer(many=True)

    class Meta:
        model = OrderInfo
        fiedls = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    pay_status = serializers.CharField(read_only=True)
    trade_no = serializers.CharField(read_only=True)
    order_sn = serializers.CharField(read_only=True)
    pay_time = serializers.DateTimeField(read_only=True)

    def generate_order_sn(self):
        from random import Random
        random_ins = Random()
        order_sn = "{time_str}{userid}{ranstr}".format(time_str=time.strftime("%Y%m%d%H%M%S"),
                                                       userid=self.context['request'].user.id,
                                                       ranstr=random_ins.randint(10, 99))
        return order_sn

    def validate(self, attrs):
        attrs['order_sn'] = self.generate_order_sn()
        return attrs

    class Meta:
        model = OrderInfo
        fields = '__all__'