from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path, include
from .views import WarehouseViewSet, WarehouseProductViewSet, MovementViewSet, MovementItemViewSet

router = SimpleRouter()


router.register("warehouse", WarehouseViewSet)
router.register("warehouseproduct", WarehouseProductViewSet)
router.register('movement', MovementViewSet)
router.register('movementitem', MovementItemViewSet)


urlpatterns = [
]