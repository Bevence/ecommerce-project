from ecommerce.models import Items, Category, Subcategory


def categories(request):
    category_list = Category.objects.all()
    return {"categories": category_list}


def subcategories(request):
    category_list = Category.objects.all()
    sub_categories_list = {}
    for category in category_list:
        sub_categories_list[category.title] = Subcategory.objects.filter(category=category)
    return {"sub_categories_list": sub_categories_list}
