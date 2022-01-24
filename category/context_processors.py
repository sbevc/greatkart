from category.models import Category


def product_categories(request):
    categories = Category.objects.all()
    return {"product_categories": categories}
