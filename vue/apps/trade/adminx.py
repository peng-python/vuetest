import xadmin
from .models import ShopCart, OrderInfo, OrderDetail


class ShopCartAdmin(object):
    list_display = ['user', 'goods', 'nums', 'add_time']
    list_filter = ['user', 'goods', 'nums']
    search_fields = ['user', 'goods', 'nums', 'add_time']


class OrderInfoAdmin(object):
    list_display = ['user', 'order_sn', 'trade_sn', 'pay_status', 'post_script',
                    'order_mount', 'pay_time', 'add_time']
    list_filter = ['user', 'order_sn', 'trade_sn', 'pay_status', 'post_script',
                   'order_mount', 'pay_time']
    search_fields = ['user', 'order_sn', 'trade_sn', 'pay_status', 'post_script',
                     'order_mount', 'pay_time', 'add_time']



class OrderDetailAdmin(object):
    list_display = ['order', 'goods', 'goods_num', 'add_time']
    list_filter = ['order', 'goods', 'goods_num']
    search_fields =['order', 'goods', 'goods_num', 'add_time']


xadmin.site.register(ShopCart, ShopCartAdmin)
xadmin.site.register(OrderInfo, OrderInfoAdmin)
xadmin.site.register(OrderDetail, OrderDetailAdmin)