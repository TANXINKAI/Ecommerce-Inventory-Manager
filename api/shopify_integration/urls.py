"""
shopify integration urls
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shopify_integration.views import shopify_login, shopify_callback, AccountViewSet, shopify_products, \
    shopify_product_update, shopify_product_export

router = DefaultRouter()
router.register(r'shopify_shop', AccountViewSet)

urlpatterns = [
    path('login/', shopify_login),
    path('callback/', shopify_callback),
    path('', include(router.urls)),
    path('products/', shopify_products),
    path('product/update/', shopify_product_update),
    path('products/export/', shopify_product_export),
]
