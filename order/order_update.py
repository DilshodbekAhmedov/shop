from order.models import Order, OrderItem
from django.db.models import Sum


def add_all_total(id):
    order_item_agg = OrderItem.objects.filter(order_id=id).aggregate(amount_total=Sum('total'))
    order_obj = Order.objects.get(id=id)
    order_obj.total = order_item_agg.get('amount_total')
    order_obj.save()