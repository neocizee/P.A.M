from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('testToken', views.token),
    re_path('arboles', views.listaArboles),
    re_path('agregarArbol', views.agregarArbol),
    re_path('listaAForeign', views.listaAForeign),
    re_path('borrarArbol', views.borrarArbol),
    re_path('editarArbol', views.editarArbol)
]
