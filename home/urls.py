from unicodedata import name
from django.urls import path,include
from .import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name='home'

urlpatterns = [
    path('', views.home, name='home'),
    path('index.html', views.contact_create, name='home'),
    path('lodge.html', views.lodge, name='lodge'),
    path('services.html', views.services, name='services'),
    path('camping.html', views.camping, name='camping'),
    path('about.html', views.about_create, name='about'),
   # path('contact.html', views.contact_create, name='contact_create'), 
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns=urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
