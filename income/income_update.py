from django.db.models import Sum, Subquery

from income.models import IncomeItem, Income


def add_all_total(id):
    income_items_agg = IncomeItem.objects.filter(income_id=id).aggregate(amount_total=Sum('total'))
    income_obj = Income.objects.get(id=id)
    income_obj.total = income_items_agg['amount_total']
    income_obj.save()
    #
    # income_items_agg = IncomeItem.objects.filter(income_id=id).aggregate(amount_total=Sum('total'))
    # Income.objects.filter(id=id).update(total=income_items_agg.amount_total)
    #
    # Income.objects.filter(id=id).update(total=Subquery(
    #     IncomeItem.objects.filter(income_id=id).values('income_id')
    #     .annotate(amount_total=Sum('total')).values('amount_total')[:1]
    # ))


