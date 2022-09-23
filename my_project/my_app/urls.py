from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.games, name='games'),
    path('register/', views.register, name='register'),
    path('docad/', views.docad, name='docad'),
]