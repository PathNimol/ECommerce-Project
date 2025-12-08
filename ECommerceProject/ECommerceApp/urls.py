from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'banners', TblBannerView)
router.register(r'imagetypes', ImageTypeView)
router.register(r'images', ImageView)
router.register(r'menus', MenuView)
router.register(r'menudetails', MenuDetailView)
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('productdetails', ProductDetailViewSet)
router.register('productdetailimages', ProductDetailImageViewSet)

router.register('qrcodes', QRCodeViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('show/', show_api_data, name='show_data'),

    path('banner-crud/', show_banner_crud, name='banner_crud'),
    path('image-menu-crud/', show_image_menu_crud, name='image_menu_crud'),
    path('show_menu_detail_crud/', show_menu_detail_crud, name='show_menu_detail_crud'),
    path('CarouselImageAPI/', CarouselImageAPI, name='CarouselImageAPI'),
    path('MenuClickToLoadMenuDetail/', MenuClickToLoadMenuDetail, name='MenuClickToLoadMenuDetail'),
    path('ListProductWithAddToCartCheckoutOrder/', ListProductWithAddToCartCheckoutOrder, name='ListProductWithAddToCartCheckoutOrder'),
    path('ECommerceBackEnd/', ECommerceBackEnd, name='ECommerceBackEnd'),
    path('ECommerceFrontEnd/', ECommerceFrontEnd, name='ECommerceFrontEnd'),






]