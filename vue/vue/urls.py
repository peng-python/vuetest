"""vue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from vue.settings import MEDIA_ROOT
from django.views.static import serve
import xadmin

from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from users.views import UserViewSet
from goods.views import GoodsViewSet, CategoryViewSet
from user_operation.views import UserFavViewSet, AddressViewSet, LeavingMessageViewSet
from trade.views import ShopCartViewSet, OrderViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet, base_name='users')
router.register(r'categorys', CategoryViewSet, base_name='categorys')
router.register(r'goods', GoodsViewSet, base_name='goods')
router.register(r'userfavs', UserFavViewSet, base_name='userfavs')
router.register(r'address', AddressViewSet, base_name='address')
router.register(r'messages', LeavingMessageViewSet, base_name='messages')
router.register(r'shopcarts', ShopCartViewSet, base_name='shopcarts')
router.register(r'orders', OrderViewSet, base_name='orders')


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^login/', obtain_jwt_token),
]
