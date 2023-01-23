from django.urls import path
from . import views

urlpatterns = [
  
    path('appUser/', views.login, name='login'),
    path('appUser/select/', views.select, name='select'),
    path('logout/',views.logout,name='logout'),

]