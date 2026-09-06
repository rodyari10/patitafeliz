from django.contrib import admin
from django.urls import path
from mascotas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('mascotas/', views.lista_mascotas, name='lista_mascotas'),
    path('mascotas/<int:pk>/', views.detalle_mascota, name='detalle_mascota'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('adoptar/', views.adoptar, name='adoptar'),
]
