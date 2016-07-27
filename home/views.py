# -*- coding: utf-8 -*-

from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import loader
from django.template.context import RequestContext
from django.views.generic.base import TemplateView

from products.views import title


# Create your views here.

class HomeView(TemplateView):
    template_name = 'home/hoIndex.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['title'] = title
        context['seconTitle'] = 'Vista generica para visualizar información'
        return context