# -*- coding: utf-8 -*-

from django.shortcuts import (render, get_object_or_404)
from django.template import loader
from django.http import (HttpResponse, HttpResponseRedirect)
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (TemplateView, ListView, DetailView)
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)

from .forms import (ProductForm)
from .models import (Product, ImageProduct)

# Create your views here.

title = 'Django - class-base views'


# def inicial_index(request):
#     product = Product.objects.order_by('id')
#     template = loader.get_template('products/prindex.html')
#     context = {
#         'title': 'Ejercicio DJango',
#         'seconTitle': 'Modulo Productos',
#         #'product': product
#     }
#     return HttpResponse(template.render(context, request))


class ProductView(TemplateView):
    template_name = 'products/prView.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductView, self).get_context_data(*args, **kwargs)
        context['prActive'] = 'active'
        context['title'] = title
        context['seconTitle'] = 'Vista generica para visualizar información'
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'products/prList.html'
    # paginate_by = 1

#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object(queryset=Product.objects.all())
#         return super(ProductListView, self).get(request, *args, **kwargs)
#
    def get_queryset(self, *args, **kwargs):
        qs = self.model.objects.filter()
        #qs = super(ProductListView, self).get_queryset(*args, **kwargs).order_by('-name')
        #qs = super(ProductListView, self).get_queryset(*args, **kwargs).filter(name__startswith='o').order_by('-name')
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        context['prActive'] = 'active'
        context['title'] = title
        context['seconTitle'] = 'Listado de productos'
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/prDetail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetail, self).get_context_data(*args, **kwargs)
        context['prActive'] = 'active'
        context['title'] = title
        context['seconTitle'] = 'Detalle del producto'
        context['gallery'] = ImageProduct.objects.filter(producto=self.object)  
        return context


class ProductCreat(CreateView):
    #model = Product
    #fields = ['name', 'description', 'category', 'image']
    form_class = ProductForm
    template_name = 'products/prFormulario.html'
    success_url = reverse_lazy('productos:list')

#     def form_valid(self, form):
#         #jaja = 'Hola qui estamoss'
#         #sformulario = super(ProductCreat, self).clean()
#         #return ProductCreat.form_valid(self, form)(self)
#
#         return super(ProductCreat, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ProductCreat, self).get_context_data(*args,**kwargs)
        context['prActive'] = 'active'
        context['title'] = title
        context['seconTitle'] = 'Crear nuevo producto'
        context['bottonTitle'] = 'Crear Producto'
        return context


class ProducrtUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    #fields = ['name', 'description', 'image', 'category']
    template_name = 'products/prFormulario.html'
    success_url = reverse_lazy('productos:list')


    def get_context_data(self, *args, **kwargs):
        context = super(ProducrtUpdate, self).get_context_data(*args,**kwargs)
        context['prActive'] = 'active'
        context['title'] = title
        context['seconTitle'] = 'Editar producto'
        context['bottonTitle'] = 'Editar Producto'
        return context


class ProductDelete(DeleteView):
    model = Product
    template_name = 'products/prDelete.html'
    success_url = reverse_lazy('productos:list')
#    fields = ['pr_name', 'pr_description', 'pr_image', 'pr_category']

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDelete, self).get_context_data(*args,**kwargs)
        context['prActive'] = 'active'
        context['title'] = title
        context['seconTitle'] = 'Eliminar producto'
        context['bottonTitle'] = 'Eliminar Producto'
        return context
