from _decimal import Decimal
from rest_framework import status
from provider.models import Provider
from rest_framework.viewsets import ModelViewSet
from order.models import Order
from client.models import Client
from income.models import Income
from .models import OutlayCategory, Outlay, PaymentTransaction
from .serializers import OutlayCategorySerializer, OutlaySerializer, PaymentTransactionSerializer
from rest_framework.response import Response


class OutlayCategoryViewSet(ModelViewSet):
    queryset = OutlayCategory.objects.all()
    serializer_class = OutlayCategorySerializer


class OutlayViewSet(ModelViewSet):
    queryset = Outlay.objects.all()
    serializer_class = OutlaySerializer


class PaymentTransactionViewSet(ModelViewSet):
    queryset = PaymentTransaction.objects.all()
    serializer_class = PaymentTransactionSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        amount = Decimal(request.data['amount'])
        income_obj = request.data['income']
        order_obj = request.data['order']
        client_obj = request.data['client']
        provider_obj = request.data['provider']
        transaction_type = request.data['transaction_type']
        if transaction_type == 'outcome':
            amount *= -1
        if income_obj:
            income = Income.objects.get(id=income_obj)
            provider = income.provider
            provider.balance += amount
            provider.save()
        elif provider_obj:
            provider = Provider.objects.get(id=provider_obj)
            provider.balance += amount
            provider.save()
        elif order_obj:
            order = Order.objects.get(id=order_obj)
            client = order.client
            client.balance += amount
        elif client_obj:
            client = Client.objects.get(id=client_obj)
            client.balance += amount
            client.save()
        return response

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        amount = instance.amount
        transaction_type = instance.transaction_type
        income_obj = instance.income
        provider_obj = instance.provider
        order_obj = instance.order
        client_obj = instance.client
        if transaction_type == 'income':
            amount *= -1
        if income_obj:
            provider = income_obj.provider
            provider.balance += amount
            provider.save()
        elif provider_obj:
            provider_obj.balance += amount
            provider_obj.save()
        elif order_obj:
            client = order_obj.client
            client.balance += amount
        elif client_obj:
            client_obj.balance += amount
            client_obj.save()
        instance.is_deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


