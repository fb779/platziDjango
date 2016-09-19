# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from .models import (Category, Product, ImageProduct)

cl_inputs = 'form-control'

class ProductAdminForm(ModelForm):
#     name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Digite el nompre del producto completo'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Realice una breve descripcion del producto'}))
    class Meta:
        model = Product
        fields = ('name','description')

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
                'placeholder': 'Nombres completos',
                'class': cl_inputs
            }),
            'description': forms.Textarea(attrs={
                'id': 'desProduct',
                'placeholder': 'Digitar una descricion completa del producto',
                'class': cl_inputs
            }),
            'category': forms.Select(attrs={
                'id': 'catProduct',
                'class': cl_inputs
            }),
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # adicionar mensajes personalizados de los errores
        self.fields['name'].error_messages = {'required': 'El nombre no puede estar vacio!'}
        self.fields['description'].error_messages = {'required': 'La descripcion no puede estar vacia!'}
        self.fields['category'].error_messages = {'required': 'Debe seleccionar una categoria!'}



    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if name == '':
    #         raise forms.ValidationError("El nombre no puede estar vacio")
    #     return name

    def clean(self):
        self.cleaned_data = super(ProductForm, self).clean()
        nombre = self.cleaned_data.get('name')
        descri = self.cleaned_data.get('description')
        print self.cleaned_data

        # if nombre == '':
        #     self._errors['name'] = self.error_class(['Este campo es obligatorio.'])

        # if descri == '':
        #     self._errors['description'] = self.error_class(['El campo de descripcion es obligatorio'])

        return self.cleaned_data

class ImageProductForm(ModelForm):
    class Meta:
        model = ImageProduct
        fields = ('__all__')


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('__all__')
