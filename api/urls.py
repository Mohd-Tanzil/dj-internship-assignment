from django.urls import path
from .views import public_api

urlpatterns = [
    path('public/', public_api, name='public-api'),
]
