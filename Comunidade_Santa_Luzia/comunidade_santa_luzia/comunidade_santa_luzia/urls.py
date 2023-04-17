
from django.urls import path
from app_santa_luzia import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('/contatos', views.contatos, name='contatos'),
    path('/pastorais', views.pastorais, name= 'pastorais')
]
