from django.urls import path
from . import views 
from django.http import JsonResponse

urlpatterns = [
    path('',views.save_data,name='saves'),
]