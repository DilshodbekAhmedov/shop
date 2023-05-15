"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from client.urls import router as client_router
from django.conf import settings
from core.router import DefaultRouter
from income.urls import router as income_router
from order.urls import router as order_router
from product.urls import router as product_router
from provider.urls import router as provider_router
from user.urls import router as user_router
from warehouse.urls import router as warehouse_router
from payment.urls import router as payment_router
from user.views import RegisterAPI, VerifyOTP
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = DefaultRouter()
router.extend(client_router)
router.extend(income_router)
router.extend(order_router)
router.extend(provider_router)
router.extend(product_router)
router.extend(warehouse_router)
router.extend(user_router)
router.extend(payment_router)

schema_view = get_schema_view(
   openapi.Info(
      title="ONLINE MARKET API",
      default_version='v1',
      description="Online market discretion",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="hyperman0011@gamil.com"),
      license=openapi.License(name="hyperman license"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterAPI.as_view()),
    path('verify/', VerifyOTP.as_view()),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('set_base/', set_base, name='set_base'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()