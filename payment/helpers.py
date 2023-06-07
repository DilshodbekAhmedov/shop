from client.models import Client
from income.models import Income
from order.models import Order
from payment.models import Outlay
from provider.models import Provider


def define_payment_transaction_obj(payment_type, obj):
    body = {}
    if payment_type == "income" or obj.income is not None:
        income = Income.objects.get(id=obj.income_id)
        body["Tovar kirimi uchun xarajat"] = {
            "Yetkazib beruvchi ismi": income.provider.name,
            "Yetkazib beruvchi tel. raqami": income.provider.phone,
        }
    if payment_type == "order" or obj.order is not None:
        order = Order.objects.get(id=obj.order_id)
        body["Zakaz uchun kirim"] = {
            "Xaridor ismi": order.client.full_name,
            "Xaridor tel. raqami": order.client.phone,
            "Zakaz holati": order.get_status_display(),
            "Zakaz summasi": str(order.total),
        }
    if payment_type == "client" or obj.client is not None:
        client = Client.objects.get(id=obj.client_id)
        body["Doimiy xaridordan qilingan savdo"] = {
            "Xaridor ismi": client.full_name,
            "Xaridor tel. raqami": client.phone,
            "Xaridor balansi": str(client.balance),
        }
    if payment_type == "provider" or obj.provider is not None:
        provider = Provider.objects.get(id=obj.provider_id)
        body["Yetkazib beruvchi oldi-berdisi"] = {
            "Yetkazib beruvchi ismi": provider.name,
            "Yetkazib beruvchi tel. raqami": provider.phone,
            "Yetkazib beruvchi balansi": str(provider.balance),
        }
    if payment_type == "outlay" or obj.outlay is not None:
        outlay = Outlay.objects.get(id=obj.outlay_id)
        body["Xarajatlar ro'yxati"] = {
            "Xarajat nomi": outlay.name,
            "Xarajat kategoriya nomi": outlay.outlay_category.name,
        }
    return body
