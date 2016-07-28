from django.conf.urls import url
from . import views as hoViews

urlpatterns = [
    url(r'^$', hoViews.fn_index, name='index'),
#     url(r'^principal/$', hoViews.HomeView.as_view(), name='principal'),
#     url(r'^listado$', prViews.ProductListView.as_view(), name='list'),
#     url(r'^detalle/(?P<pk>\d+)$', prViews.ProductDetail.as_view(), name='detail'),
#     url(r'^nuevo/$', prViews.ProductCreat.as_view(), name='new'),
#     url(r'^editar/(?P<pk>\d+)$', prViews.ProducrtUpdate.as_view(), name='edit'),
#     url(r'^borrar/(?P<pk>\d+)$', prViews.ProductDelete.as_view(), name='delete'),
]
