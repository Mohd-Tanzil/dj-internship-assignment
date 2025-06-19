from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def public_api(request):
    return Response({"message": "This is a public API. Anyone can access it!"})
