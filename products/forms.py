# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from .models import (Category, Product, ImageProduct)



class ProductForm(ModelForm):
#     name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Digite el nompre del producto completo'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Realice una breve descripcion del producto'}))
    class Meta:
        model = Product
        fields = ('__all__')
        #fields = ('name','description', 'image', 'category')
        widgets = {
            'name': forms.TextInput(attrs = {
                'id': 'nomProduct',
                'placeholder': u'Nombres completos',
                'class': 'center' 
            }),
            'description': forms.Textarea(attrs={
                'id': 'desProduct',
                'placeholder': 'Digitar una descricion completa del producto'
            })
        }
    
    def clean(self):
        self.cleaned_data = super(ProductForm, self).clean()
        nombre = self.cleaned_data.get('name')
        descri = self.cleaned_data.get('description')

        if nombre == '':
            self._errors['name'] = self.error_class(['Este campo es obligatorio.'])
        
        if descri == '':
            self._errors['description'] = self.error_class(['El campo de descripcion es obligatorio'])

        return self.cleaned_data

class ImageProductForm(ModelForm):
    class Meta:
        model = ImageProduct
        fields = ('__all__')


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('__all__')
