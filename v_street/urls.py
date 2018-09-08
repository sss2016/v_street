"""v_street URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import Shops.Controller.index as Index
import Shops.Controller.file as File
import Shops.Controller.goods as Goods
import Shops.Controller.shopping as Shopping
import Shops.Controller.user as User
# from Shops.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('shop/', getShop),
    path('', Index.showIndex),
    path('getGoodsList',Index.getGoodsList),
    path('uploadImage',File.upload_image),
    path('addGoods',Goods.addGoods),
    path('getGoodsImage',File.getGoodsImage),
    path('getGoodsTypes',Goods.getGoodsType),
    path('addType',Goods.addType),
    path('deleteType',Goods.deleteType),
    path('getGoodsItem',Goods.getGoodsItem),
    path('updateItem',Goods.updateItem),
    path('deleteGoods',Goods.deleteGoods),
    path('getShops',Shopping.getShops),
    path('getFrontShopsInfo',Goods.getFrontGoodsByshopId),
    path('submitOrder',Shopping.submitOrder),
    path('getOrderList',Shopping.getOrderList),
    path('cancelOrder',Shopping.cancelOrder),
    path('getMyAddreses',User.getMyAddreses),
    path('addMyAddreses',User.addMyAddreses),
    path('updateMyAddreses',User.updateMyAddreses),
    path('delMyAddreses',User.delMyAddreses),
    path('getDefaultAddr',User.getDefaultAddr),
    path('updateChecked',User.updateChecked),
    path('getOrderDetail',Shopping.getOrderDetail),
    path('userauthor',User.userauthor),
    path('setUserInfo',User.setUserInfo),
    path('ShopFilter',Shopping.ShopFilter),
    path('FeedBack',User.FeedBack),
    path('getSwiper',Index.getSwiper),
    path('getShopDetail',Shopping.getShopDetail),
        
]
