from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Arbolado, Vereda_estado, Arbol_estado, Arbol_especie, Arbol_area_detalles

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']
        
        
class ArboladoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arbolado
        fields = '__all__'
