from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from home.models import users
from .serializers import usersSerializer

# Create your views here.

@api_view(['GET'])
def getData(request):
    user=users.objects.all()
    serializer=usersSerializer(user, many=True)
    return Response(serializer.data)



