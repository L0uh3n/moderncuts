from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('log_reg/', views.log_reg, name='log_reg'),
    path('logout/', views.logout, name='logout'),
    path('login_error/', views.login_error, name='login_error'),
    path('register_sucess/', views.register_sucess, name='register_sucess'),
    path('register_error/', views.register_error, name='register_error'),
    path('docad/', views.docad, name='docad'),
    path('dolog/', views.dolog, name='dolog'),
    path('doout/', views.doout, name='doout'),
    path('profile/', views.profile, name='profile'),
    path('doupdate/', views.doupdate, name='doupdate'),
    path('coment/', views.coment, name='coment'),
    path('coment/<int:id>/editar/', views.edit_coment, name='edit_coment'),
    path('agend/', views.agend, name='agend'),
]