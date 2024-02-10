from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('location/', views.location, name='location'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('signup/', views.registerUser, name='signup'),

]
