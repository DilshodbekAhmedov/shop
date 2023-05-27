from rest_framework.routers import SimpleRouter

from .views import WarehouseProductViewSet

router = SimpleRouter()

router.register("warehouseproduct", WarehouseProductViewSet)



urlpatterns = [
]