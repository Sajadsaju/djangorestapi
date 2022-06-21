from .models import Enpdata
from django.shortcuts import get_object_or_404,render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from  .serializers import *


@api_view(['GET'])
def Home(request):
    return Response('Hellow World')
@api_view(['GET'])
def Apilist(request):
    api=Enpdata.objects.all()
    serializers=ApiSerializer(api,many=True)
    return Response(serializers.data)

@api_view(['POST'])      
def Create(request):
    serializer=ApiSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
        return Response('item added')

@api_view(['POST'])
def Update(request,pk):
    serializer=Enpdata.objects.get(pk=pk)
    data=ApiSerializer(instance=serializer,data=request.data)
    if(data.is_valid()):
        data.save()
        return Response('item updated')


@api_view(['DELETE'])
def Delete(request,pk):
    serializer=get_object_or_404(Enpdata,pk=pk)
    # data=ApiSerializer(instance=serializer,data=request.data)
    serializer.delete()
    return Response('item deleted')        