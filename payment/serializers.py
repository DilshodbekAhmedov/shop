from rest_framework.serializers import ModelSerializer
from .models import OutlayCategory, Outlay, PaymentTransaction


class OutlayCategorySerializer(ModelSerializer):

    class Meta:
        model = OutlayCategory
        fields = "__all__"


class OutlaySerializer(ModelSerializer):

    class Meta:
        model = Outlay
        fields = "__all__"


class PaymentTransactionSerializer(ModelSerializer):

    class Meta:
        model = PaymentTransaction
        fields = "__all__"
