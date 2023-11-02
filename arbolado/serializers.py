from rest_framework import serializers
from django.contrib.auth.models import User
from arb_datos.models import Arbolado

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']
        
        
class ArboladoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arbolado
        fields = '__all__'