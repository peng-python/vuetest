from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model

from goods.models import GoodsModel

User = get_user_model()

# Create your models here.


class ShopCart(models.Model):
    user = models.ForeignKey(User, verbose_name='用户')
    goods = models.ForeignKey(GoodsModel, verbose_name='商品')
    nums = models.IntegerField(default=0, verbose_name='购买数量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
        unique_together = ('user', 'goods')

    def __str__(self):
        return '%s(%d)'.format(self.goods.name, self.nums)


class OrderInfo(models.Model):
    ORDER_STATUS = (
        ('TRADE_SUCCESS', '成功'),
        ('TRADE_CLOSED', '超时关闭'),
        ('WAIT_BUYER_PAY', '交易创建'),
        ('TRADE_FINISHED', '交易结束'),
        ('paying', '待支付'),
    )
    user = models.ForeignKey(User, verbose_name='用户')
    order_sn = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name='订单号')
    trade_sn = models.CharField(max_length=100, unique=True, null=True, verbose_name='交易号')
    pay_status = models.CharField(max_length=30, choices=ORDER_STATUS, default='paying', verbose_name='订单状态')
    post_script = models.CharField(max_length=200, default='', verbose_name='订单留言')
    order_mount = models.FloatField(default=0.0, verbose_name='订单金额')
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name='支付时间')

    address = models.CharField(max_length=100, default='', verbose_name='收货地址')
    signer_name = models.CharField(max_length=20, default='', verbose_name='签收人')
    signer_mobile = models.CharField(max_length=11, default='', verbose_name='联系电话')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)


class OrderDetail(models.Model):
    order = models.ForeignKey(OrderInfo, related_name='goods', verbose_name='订单信息')
    goods = models.ForeignKey(GoodsModel, verbose_name='商品')
    goods_num = models.IntegerField(default=0, verbose_name='商品数量')

    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)