from django.shortcuts import render, redirect
from .models import Phone



def index(request):
    return redirect('catalog')


def show_catalog(request):
    phone_list = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort is None:
        phone_list = phone_list
    elif sort == 'max_price':
        phone_list = Phone.objects.order_by('-price')
    elif sort == 'min_price':
        phone_list = Phone.objects.order_by('price')
    else:
        phone_list = Phone.objects.order_by('name')
    template = 'catalog.html'
    context = {'phones': phone_list}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_list = Phone.objects.filter(slug=slug).values()
    context = {'phone': phone_list[0]}
    return render(request, template, context)
