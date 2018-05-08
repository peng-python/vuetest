from django.db import models
from DjangoUeditor.models import UEditorField
from datetime import datetime

# Create your models here.


# class GoodsCategoryFirst(models.Model):
#     name = models.CharField(default='', max_length=30, help_text='一级类别', verbose_name='一级类别')
#     # son_category = models.ForeignKey(GoodsCategorySecond, default='', verbose_name='子类别')
#     code = models.CharField(default='', max_length=30, help_text='类别code', verbose_name='类别code')
#     desc = models.TextField(default='', help_text='类别描述', verbose_name='类别描述')
#     is_tab = models.BooleanField(default=False, help_text='是否导航', verbose_name='是否导航')
#     add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
#
#     class Meta:
#         verbose_name = '一级类别'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name
#
#
# class GoodsCategorySecond(models.Model):
#     name = models.CharField(default='', max_length=30, help_text='二级类别', verbose_name='二级类别')
#     parent_category = models.ForeignKey(GoodsCategoryFirst, related_name='sub_cat',verbose_name='父级类别')
#     # son_category = models.ForeignKey(GoodsCategoryThird, default='', verbose_name='子类别')
#     code = models.CharField(default='', max_length=30, help_text='类别code', verbose_name='类别code')
#     desc = models.TextField(default='', help_text='类别描述', verbose_name='类别描述')
#     add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
#
#     class Meta:
#         verbose_name = '二级类别'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name
#
#
# class GoodsCategoryThird(models.Model):
#     name = models.CharField(default='', max_length=30, help_text='三级类别', verbose_name='三级类别')
#     parent_category = models.ForeignKey(GoodsCategorySecond, related_name='sub_cat', verbose_name='父级类别')
#     code = models.CharField(default='', max_length=30, help_text='类别code', verbose_name='类别code')
#     desc = models.TextField(default='', help_text='类别描述', verbose_name='类别描述')
#     add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
#
#     class Meta:
#         verbose_name = '三级类别'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name
class GoodsCategory(models.Model):
    CATEGORY_TYPE = (
        (1, '一级类目'),
        (2, '二级类目'),
        (3, '三级类目'),
    )
    name = models.CharField(default='', max_length=30, help_text='类别名', verbose_name='类别名')
    code = models.CharField(default='', max_length=30, help_text='类别code', verbose_name='类别code')
    desc = models.TextField(default='', help_text='类别描述', verbose_name='类别描述')
    category_type = models.IntegerField(choices=CATEGORY_TYPE, help_text='类目级别', verbose_name='类目级别')
    parent_category = models.ForeignKey('self', null=True, blank=True, help_text='父目录',
                                        related_name='sub_cat', verbose_name='父目录')
    is_tab = models.BooleanField(default=False, help_text='是否加入顶部导航栏', verbose_name='是否加入顶部导航栏')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '商品类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='商品名')
    category = models.ForeignKey(GoodsCategory, verbose_name='所属类别')
    goods_sn = models.CharField(max_length=50, default='', verbose_name='商品唯一货号')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    sold_num = models.IntegerField(default=0, verbose_name='商品销售量')
    fav_num = models.IntegerField(default=0, verbose_name='收藏数')
    goods_num = models.IntegerField(default=0, verbose_name='库存数')
    market_price = models.FloatField(default=0, verbose_name='市场价')
    shop_price = models.FloatField(default=0, verbose_name='本店售价')
    goods_brief = models.TextField(max_length=500, verbose_name='商品简短描述')
    goods_desc = UEditorField(default='', imagePath='goods/images/', filePath='goods/files/', width=1000, height=300,
                              verbose_name='内容')
    ship_free = models.BooleanField(default=True, verbose_name='是否承担运费')
    goods_front_image = models.ImageField(upload_to='goods/images/', null=True, blank=True, verbose_name='封面图')
    is_new = models.BooleanField(default=False, verbose_name='是否为新品')
    is_hot = models.BooleanField(default=False, verbose_name='是否为热销')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name