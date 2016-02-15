from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views as prViews

urlpatterns = [
    #url(r'^$', prViews.inicial_index, name='index'),
    url(r'^$', prViews.ProductListView.as_view(),
        name='list'),
    url(r'^product/(?P<pk>\d+)$', prViews.ProductDetail.as_view(), name='detail'),
    url(r'^product/nuevo/$', prViews.ProductCreat.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', prViews.ProducrtUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', prViews.ProductDelete.as_view(), name='delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
