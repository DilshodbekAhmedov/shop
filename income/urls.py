from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path, include
from .views import IncomeViewSet, IncomeItemViewSet

router = SimpleRouter()

router.register("income", IncomeViewSet)
router.register("incomeitem", IncomeItemViewSet)

urlpatterns = [

]
