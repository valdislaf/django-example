from django.urls import path
from django.conf.urls import include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    # path('news/', views.news, name='news'),
    path('symbols/', views.symbols, name='symbols'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
