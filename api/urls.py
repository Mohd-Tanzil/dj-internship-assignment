from django.urls import path
from .views import public_api, protected_api, home_view

urlpatterns = [
    path('public/', public_api, name='public-api'),
    path('', home_view, name='home'), 
    path('protected/', protected_api, name='protected-api'), 
]


