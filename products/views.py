from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

from .forms import (ProductForm, CategoryForm)
from .models import (Category, Product)

# Create your views here.

def inicial_index(request):
    product = Product.objects.order_by('id')
    template = loader.get_template('index.html')
    context = {
        'title': 'Ejercicio DJango',
        'product': product
    }
    return HttpResponse(template.render(context, request))