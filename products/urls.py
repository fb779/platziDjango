from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views as prViews

urlpatterns = [
    url(r'^$', prViews.inicial_index, name='index'),
    url(r'^lista-productos/$', prViews.ProductListView.as_view(), name='lista-productos'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
