from django.conf.urls import url
from . import views as prViews

urlpatterns = [
    url(r'^$', prViews.inicial_index, name='index'),
]
