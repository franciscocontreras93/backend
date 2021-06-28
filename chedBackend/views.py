from django.shortcuts import render
from django.core.serializers import serialize
from chedBackend.models import TiendasChedraui
from chedBackend.serializers import TiendasSerializer

from django.http.response import HttpResponse, JsonResponse
from rest_framework import status 
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def tiendas_list(request):
    # GET list of Tiendas, POST a new Tienda, DELETE all Tiendas
    # if request.method == 'GET':
    #     _TDA_ = TiendasChedraui.objects.all()
    #     # tiendas_serializer = TiendaSerializer(tiendas, many=True)
    #     # THIS CODE ADD \" IN THE RESULT SOLVE IT
    #     _SERIALIZER_ = serialize('geojson', _TDA_)
    #     return HttpResponse(_SERIALIZER_)
    if request.method == 'GET':
        tiendas = TiendasChedraui.objects.all()
        _serializer_ = TiendasSerializer(tiendas, many=True)
        return JsonResponse(_serializer_.data, safe=False)
        # 'safe=False' for objects serialization


@api_view(['GET', 'PUT', 'DELETE'])
def tiendas_detalle(request, id_mg):
    try:
        _TDA_ = TiendasChedraui.objects.filter(id_mg=id_mg)
    except _TDA_.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        _SERIALIZER_ = serialize('geojson', _TDA_)
        return HttpResponse(_SERIALIZER_)
    pass










# Create your views here.



