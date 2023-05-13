from rest_framework.viewsets import ModelViewSet
from .models import Client
from .serializers import ClientSerializer
from rest_framework import filters
from django_filters import rest_framework as filters


class ClientFilter(filters.FilterSet):
    status = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Client
        fields = ("id", 'full_name')


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filterset_class = ClientFilter



