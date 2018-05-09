import xadmin
from .models import UserFav, UserAddress, UserLeavingMessage


class UserFavAdmin(object):
    list_display = ['user', 'goods', 'add_time']
    list_filter = ['user', 'goods']
    search_fields = ['user', 'goods', 'add_time']


class UserAddressAdmin(object):
    list_display = ['user', 'province', 'city', 'district', 'address', 'signer_name', 'signer_mobile', 'add_time']
    list_filter = ['user', 'province', 'city', 'district', 'address', 'signer_name', 'signer_mobile']
    search_fields = ['user', 'province', 'city', 'district', 'address', 'signer_name', 'signer_mobile', 'add_time']


class UserLeavingMessageAdmin(object):
    list_display = ['user', 'message_type', 'subject', 'message', 'add_time']
    list_filter = ['user', 'message_type', 'subject', 'message']
    search_fields = ['user', 'message_type', 'subject', 'message', 'add_time']


xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserAddress, UserAddressAdmin)
xadmin.site.register(UserLeavingMessage, UserLeavingMessageAdmin)