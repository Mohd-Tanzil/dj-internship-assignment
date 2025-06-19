from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def public_api(request):
    return Response({"message": "This is a public API. Anyone can access it!"})

def home_view(request):
    return HttpResponse("Welcome to the Internship API 👋")

@api_view(['GET']) 
@permission_classes([IsAuthenticated])  
def protected_api(request):
    return Response({"message": f"Hello, {request.user.username}! This is a protected API."})