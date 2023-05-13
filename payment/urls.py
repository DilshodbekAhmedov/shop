from django.urls import path
from .views import OutlayCategoryViewSet, OutlayViewSet, PaymentTransactionViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()


router.register('outlaycategory', OutlayCategoryViewSet)
router.register('outlay', OutlayViewSet)
router.register('payment', PaymentTransactionViewSet)

urlpatterns = [
]