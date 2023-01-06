from django.urls import path
from . import views

urlpatterns = [
  
    path('appUser/',views.login,name='login'),
    path('appUser/emphome/',views.emphome,name='emphome'),
    path('home/',views.admin,name='admin'),
    path('employee/',views.employee,name='employee'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile1/',views.profileadmin,name='profileadmin'),
    path('employee_registration/',views.createemp,name='createemp'),
    path('employee_registration/saveemp/',views.saveemp,name='saveemp'),
    path('employee_update/',views.updateemp,name='updateemp'), 
    path('leave_applications/',views.empleaves,name='updateemp'),
    path('leaves_structure/',views.leaves_structure,name='leaves_structure'),
]