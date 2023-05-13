from django.http import JsonResponse

from .models import Category, Product


def get_category_childes(category: Category, categories: list[Category], products: list[Product]):
    return [
        {
            'id': child_category.id,
            'name': child_category.name,
            'childes': get_category_childes(child_category,
                                            categories,
                                            products),
            'product': [
                {
                    'id': product.id,
                    'name': product.name,
                }
                for product in products
                if product.category_id == child_category.id
            ]
        }
        for child_category in categories
        if child_category.parent_id == category.id
    ]


def get_product_tree(view, request):
    get_filter = request.POST.get('get_filter')
    response_list = []
    if get_filter == 'all':
        categories = Category.objects.all().in_bulk()
        products = Product.objects.all().in_bulk()
    else:
        categories = Category.objects.filter(
            is_deleted=False,
        ).in_bulk()
        products = Product.objects.filter(
            is_deleted=False,
        ).in_bulk()

    for category in categories.values():
        if not category.parent:
            response_list.append(
                {
                    'id': category.id,
                    'name': category.name,
                    'childes': get_category_childes(category,
                                                    categories.values(),
                                                    products.values()),
                    'product': [
                        {
                            'id': product.id,
                            'name': product.name,
                        }
                        for product in products.values()
                        if product.category_id == category.id
                    ]
                }
            )
    return JsonResponse(response_list, status=200, safe=False)

print(get_product_tree())