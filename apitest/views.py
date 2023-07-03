from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
# from .models import modelname
from django.http import Http404
from rest_framework import status
from rest_framework.serializers import Serializer
from .apitest import maple_API

# Create your views here.

@api_view(['GET','POST'])
def mapleapi(request):
    if request.method == 'GET':
        datas = maple_API
        serializer = Serializer(datas)
        return Response(serializer.data)
