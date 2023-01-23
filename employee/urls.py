from django.urls import path
from . import views

urlpatterns = [
  
    path('employee/', views.employee, name='employee'),
    path('profile/',views.profile,name='profile'),
    path('leaveApplication/',views.leaveApplication,name='leaveApplication'),
    path('leaveStructure/',views.leaveStructure,name='leaveStructure')

]