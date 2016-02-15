from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView
#from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView , DeleteView)

from .forms import ProductForm, CategoryForm
from .models import Category, Product

# Create your views here.

title = 'Ejercicio Django con class-base views'

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
    paginate_by = 1

#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object(queryset=Product.objects.all())
#         return super(ProductListView, self).get(request, *args, **kwargs)
#
#     def get_queryset(self):
#         return self.object.book_set.all()

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = title
        context['seconTitle'] = 'Listado de productos'
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/prDetail.html'
    
    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['title'] = title
        context['seconTitle'] = 'Detalle del producto'
        return context


class ProductCreat(CreateView):
    model = Product
    template_name = 'products/prFormulario.html'
    success_url = reverse_lazy('productos:list')
    fields = ['pr_name', 'pr_description', 'pr_image', 'pr_category']
    
    def get_context_data(self, **kwargs):
        context = super(ProductCreat, self).get_context_data(**kwargs)
        context['title'] = title
        context['seconTitle'] = 'Crear nuevo producto'
        context['bottonTitle'] = 'Crear Producto'
        return context

class ProducrtUpdate(UpdateView):
    model = Product
    template_name = 'products/prFormulario.html'
    success_url = reverse_lazy('productos:list')
    fields = ['pr_name', 'pr_description', 'pr_image', 'pr_category']
    
    def get_context_data(self, **kwargs):
        context = super(ProducrtUpdate, self).get_context_data(**kwargs)
        context['title'] = title
        context['seconTitle'] = 'Editar producto'
        context['bottonTitle'] = 'Editar Producto'
        return context


class ProductDelete(DeleteView):
    model = Product
    template_name = 'products/prDelete.html'
    success_url = reverse_lazy('productos:list')
#    fields = ['pr_name', 'pr_description', 'pr_image', 'pr_category']
    
    def get_context_data(self, **kwargs):
        context = super(ProductDelete, self).get_context_data(**kwargs)
        context['title'] = title
        context['seconTitle'] = 'Eliminar producto'
        context['bottonTitle'] = 'Eliminar Producto'
        return context
