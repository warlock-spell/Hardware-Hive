from django.shortcuts import render
from item.models import Item, Category


# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    context = {'items': items, 'categories': categories}
    return render(request, 'core/index.html', context)


def contact(request):
    return render(request, 'core/contact.html')


def privacy_policy(request):
    return render(request, 'core/privacy-policy.html')


def terms(request):
    return render(request, 'core/terms.html')


def about(request):
    return render(request, 'core/about.html')


def careers(request):
    return render(request, 'core/careers.html')
