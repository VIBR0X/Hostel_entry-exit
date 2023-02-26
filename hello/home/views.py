from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def getData(request):
    users={'name':'Ashwin', 'roll_n0':'22b3007','hostel_no':'1','room_no':'52','hostelvisited':'3'}
    return Response(users)

   

