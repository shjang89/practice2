from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# from .serializers import ArticleListSerializer, ArticleSerializer
@api_view(['GET'])
def double_number(request, number):
    result = number * 2
    return Response({'result': result})