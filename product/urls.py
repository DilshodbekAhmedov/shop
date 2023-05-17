from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path, include
from . import views

router = SimpleRouter()
router.register('character', views.CharacterViewSet)
router.register('productcharacter', views.ProductCharactoryViewSet)
router.register('product', views.ProductViewSet)
router.register('country', views.CountryViewSet)
router.register('productmedia', views.ProductMediaViewSet)
router.register('productprice', views.ProductPriceViewSet)
router.register('category', views.CategoryViewSet)
router.register('manufactory', views.ManufactoryViewSet)

urlpatterns = [
]