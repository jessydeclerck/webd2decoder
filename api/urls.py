from django.urls import path
from . import views

urlpatterns = [
    path('fromserver', views.decodeFromServer),
    path('fromclient', views.decodeFromClient),
]
