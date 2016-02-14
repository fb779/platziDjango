from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import ListView

from .forms import (ProductForm, CategoryForm)
from .models import (Category, Product)

# Create your views here.

def inicial_index(request):
    product = Product.objects.order_by('id')
    template = loader.get_template('products/prindex.html')
    context = {
        'title': 'Ejercicio DJango',
        'seconTitle': 'Modulo Productos',
        'product': product
    }
    return HttpResponse(template.render(context, request))

class ProductListView(ListView):
    model = Product
    template_name = 'products/prList.html'
    
    #template_name = "books/publisher_detail.html"

#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object(queryset=Product.objects.all())
#         return super(ProductListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Ejercicio Django - Productos'
        context['seconTitle'] = 'Listado de productos'
        return context

#     def get_queryset(self):
#         return self.object.book_set.all()
    
    
    
    