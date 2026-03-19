from django.urls import path
from .import views

urlpatterns =[
    path('play/',views.say_hello,name = 'say_hello'),
]