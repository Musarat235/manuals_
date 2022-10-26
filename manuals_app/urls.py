from cgitb import html
from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    # path('<slug:my_id>/', views.product_manual, name='product_manual'),
    url(r'^category/(?P<hierarchy>.+)/$', views.show_category, name='category'),
    url(r'^view_pdf/$', views.pdf_view, name='pdf_view'),
    path('/index.html', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)