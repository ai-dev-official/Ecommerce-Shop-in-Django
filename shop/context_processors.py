from .models import Category


def menu_links(request):
    categories = Category.objects.filter(parent=None)

    return {'menu_links': categories}
