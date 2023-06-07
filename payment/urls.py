from django.urls import path
from .views import OutlayCategoryViewSet, OutlayViewSet, PaymentTransactionViewSet, PaymentTransactionListAPIView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()


router.register('outlaycategory', OutlayCategoryViewSet)
router.register('outlay', OutlayViewSet)
router.register('payment', PaymentTransactionViewSet)


urlpatterns = [
    path('payment_detail_list_apiview', PaymentTransactionListAPIView.as_view(), name="payment_detail_list_apiview")
]
