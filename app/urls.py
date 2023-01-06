from django.urls import path
from . import views

urlpatterns = [
  
    path('',views.login,name='login'),
    path('emphome/',views.emphome,name='emphome'),
    path('abc/',views.abc,name='abc'),
    path('adminn/',views.admin,name='admin'),
    path('employee/',views.employee,name='employee'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profileadmin/',views.profileadmin,name='profileadmin'),
    #path('createemp/',views.createemp,name='createemp'),
    path('leaveApplication/',views.leaveApplication,name='leaveApplication'),

    path('leaveStructure/',views.leaveStructure,name='leaveStructure')
]