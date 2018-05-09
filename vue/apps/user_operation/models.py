from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

from goods.models import GoodsModel

User = get_user_model()

# Create your models here.


class UserFav(models.Model):
    user = models.ForeignKey(User, verbose_name='用户')
    goods = models.ForeignKey(GoodsModel, help_text='商品的id', verbose_name='商品')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        unique_together = ('user', 'goods') # 设置联合唯一

    def __str__(self):
        return self.user.username


class UserAddress(models.Model):
    user = models.ForeignKey(User, verbose_name='用户')
    province = models.CharField(max_length=100, default='', verbose_name='省份')
    city = models.CharField(max_length=100, default='', verbose_name='城市')
    district = models.CharField(max_length=100, default='', verbose_name='区域')
    address = models.CharField(max_length=100, default='', verbose_name='详细地址')
    signer_name = models.CharField(max_length=100, default='', verbose_name='签收人')
    signer_mobile = models.CharField(max_length=11, default='', verbose_name='签收人电话')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '收货信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address


class UserLeavingMessage(models.Model):
    MESSAGE_CHOICES = (
        (1, '留言'),
        (2, '投诉'),
        (3, '询问'),
        (4, '售后'),
        (5, '求购')
    )
    user = models.ForeignKey(User, verbose_name='；用户')
    message_type = models.IntegerField(default=1, choices=MESSAGE_CHOICES,
                                       help_text='留言类型： 1(留言),2(投诉),3(询问),4(售后),5(求购)', verbose_name='留言类型')
    subject = models.CharField(max_length=100, default='', verbose_name='主题')
    message = models.TextField(default='', help_text='留言内容', verbose_name='留言内容')
    file = models.FileField(upload_to='message/file/', help_text='上传的文件', verbose_name='上传的文件')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject