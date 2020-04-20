from django.urls import path
 
from . import views

app_name = 'comms'
 
urlpatterns = [
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
]