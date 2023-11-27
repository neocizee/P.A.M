from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "No encontrado"}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data}) 

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def token(request):
    return Response("funcionando {}".format(request.user.email), status=status.HTTP_202_ACCEPTED)


from arb_datos.models import Arbolado
from django.core import serializers
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def listaArboles(request):
    arboles = serializers.serialize('json', Arbolado.objects.all())
    print(arboles)
    return Response(arboles, content_type='application/json')

from .serializers import ArboladoSerializer
@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def agregarArbol(request):
    arbol = ArboladoSerializer(data=request.data)
    if arbol.is_valid():
        arbol.save()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(arbol.errors, status=status.HTTP_400_BAD_REQUEST)

from arb_datos.models import Vereda_estado, Arbol_especie, Arbol_area_detalles, Arbol_estado
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def listaAForeign(request):
    vereda_estado = serializers.serialize('json', Vereda_estado.objects.all())
    arbol_estado = serializers.serialize('json', Arbol_especie.objects.all())
    arbol_especie = serializers.serialize('json', Arbol_especie.objects.all())
    arbol_area_detalles = serializers.serialize('json', Arbol_area_detalles.objects.all())
    return Response({vereda_estado, arbol_especie, arbol_estado, arbol_area_detalles}, content_type='application/json')


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def borrarArbol(request):
    pk = request.data["pk"]
    arbol = get_object_or_404(Arbolado, pk=pk)
    arbol.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def editarArbol(request):
    pk = request.data["pk"]
    arbol = Arbolado.objects.get(pk=pk)
    datos = ArboladoSerializer(instance=arbol, data=request.data)
    if datos.is_valid():
        datos.save()
        return Response(datos.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)