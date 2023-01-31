from django.urls import path
from . import views

urlpatterns = [
  
    path('employer/', views.employer, name='employer'),
    path('profile1/',views.profileadmin,name='profileadmin'),
    path('employee_registration/',views.createemp,name='createemp'),
    path('employee_registration/success/',views.saveemp,name='saveemp'),
    path('employee_update/',views.updateemp,name='updateemp'), 
    path('leave_applications/',views.empleaves,name='updateemp'),
    path('leaves_structure/',views.leaves_structure,name='leaves_structure'),
    path('emp_details/',views.emp_details,name='emp_details'),

    path('dept_desg/',views.department_designation,name='department_designation')

]