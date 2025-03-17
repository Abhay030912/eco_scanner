from django.urls import path
from .views import search_product  # Import the function

urlpatterns = [
    path('search/', search_product, name='search_product'),
]
