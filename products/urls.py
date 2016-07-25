from django.conf.urls import url
from . import views as prViews

urlpatterns = [
    #   url(r'^$', prViews.inicial_index, name='index'),
    url(r'^$', prViews.ProductView.as_view(), name='index'),
    url(r'^listado$', prViews.ProductListView.as_view(), name='list'),
    url(r'^detalle/(?P<pk>\d+)$', prViews.ProductDetail.as_view(), name='detail'),
    url(r'^nuevo/$', prViews.ProductCreat.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', prViews.ProducrtUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', prViews.ProductDelete.as_view(), name='delete'),
]
