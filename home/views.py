# -*- coding: utf-8 -*-

from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import loader
from django.template.context import RequestContext
from django.views.generic.base import TemplateView

from products.views import title


# Create your views here.

context = {'clActive':'active'}

def fn_index(request):
    #product = Product.objects.order_by('id')
    template = loader.get_template('home/hoIndex.html')
#     context = {
#         'clActive':'active',
#         'title': 'Ejercicio DJango',
#         'seconTitle': 'view cargada desde una funcion',
#         #'product': product
#     }
    context['title'] = 'Ejercicio DJango'
    context['seconTitle'] = 'view cargada desde una funcion'
    return HttpResponse(template.render(context, request))

# class HomeView(TemplateView):
#     template_name = 'home/hoIndex.html'
#     def get_context_data(self, *args, **kwargs):
#         context = super(HomeView, self).get_context_data(*args, **kwargs)
#         context['clActive'] = 'active'
#         context['title'] = title
#         context['seconTitle'] = 'Vista generica para visualizar información'
#         return context