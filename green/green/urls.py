from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index , name = 'index'),
    path('admin/', admin.site.urls),
    path('consultarPolo/<int:idPolo>', views.consultarPolo, name = 'consultarPolo'),
    path('cadastrarPolo', views.cadastrarPolo, name = 'cadastrarPolo'),
    path ('cadastro', views.cadastro, name= 'cadastro')

]
