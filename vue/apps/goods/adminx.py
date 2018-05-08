import xadmin
from .models import GoodsModel, GoodsCategory


class GoodsModelAdmin(object):
    list_display = ['name', 'click_num', 'sold_num', 'fav_num', 'goods_num', 'market_price', 'shop_price',
                    'goods_brief', 'goods_desc', 'is_new', 'is_hot', 'add_time']
    list_filter = ['name', 'click_num', 'sold_num', 'fav_num', 'goods_num', 'market_price', 'shop_price',
                   'goods_brief', 'goods_desc', 'is_new', 'is_hot']
    search_fields = ['name']
    style_fields = {'goods_desc': 'ueditor'}


# class GoodsCategoryFirstAdmin(object):
#     list_display = ['name', 'code', 'desc', 'is_tab', 'add_time']
#     list_filter = ['name', 'code', 'desc', 'is_tab']
#     search_fields = ['name']
#
#
# class GoodsCategorySecondAdmin(object):
#     # list_display = ['name', 'parent_category', 'code', 'desc', 'add_time']
#     # list_filter = ['name', 'parent_category', 'code', 'desc']
#     # search_fields = ['name']
#     list_display = ['name', 'son_category', 'code', 'desc', 'add_time']
#     list_filter = ['name', 'son_category', 'code', 'desc']
#     search_fields = ['name']
#
#
# class GoodsCategoryThirdAdmin(object):
#     # list_display = ['name', 'parent_category', 'code', 'desc', 'add_time']
#     # list_filter = ['name', 'parent_category', 'code', 'desc']
#     # search_fields = ['name']
#     list_display = ['name', 'code', 'desc', 'add_time']
#     list_filter = ['name', 'code', 'desc']
#     search_fields = ['name']
class GoodsCategoryAdmin(object):
    list_display = ['name', 'code', 'desc', 'category_type', 'parent_category', 'add_time']
    list_filter = ['name', 'code', 'desc', 'category_type', 'parent_category']
    search_fields = ['name', 'code', 'desc', 'category_type', 'parent_category', 'add_time']


xadmin.site.register(GoodsModel, GoodsModelAdmin)
xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
# xadmin.site.register(GoodsCategorySecond, GoodsCategorySecondAdmin)
# xadmin.site.register(GoodsCategoryThird, GoodsCategoryThirdAdmin)