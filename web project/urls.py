# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_secret_message, name='create_secret_message'),
    path('message/<uuid:pk>/', views.secret_message_detail, name='secret_message_detail'),
]
