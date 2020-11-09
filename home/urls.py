from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('<int:contato_id>', views.ver_contato, name='ver_contato'),
    path('busca', views.busca, name='busca'),
]