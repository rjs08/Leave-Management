from django.shortcuts import render

# Create your views here.
import datetime
from django.shortcuts import render, redirect
import mysql.connector as sql
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from login.models import Employee
from login.models import Leaves
from login.models import EmployeeDetails
from login.models import LeaveApplication
from employee.forms import leaveForm



def employee(request):
    return render(request, 'employee_home.html')


def profile(request):
    
    userid = request.session['user_id']
    employeeProfile = Employee.objects.filter(user=userid) 
    context={'employeeProfile':employeeProfile}
    return render(request,'profile.html',context)


def leaveApplication(request):
    
    if request.POST:  
        try:
            Date_of_application = datetime.datetime.now()
           
            form = leaveForm(request.POST)
            
            Leave_status='pending'
            userid = request.session['user_id']
        
            if form.is_valid():

                start_date = form.cleaned_data['start_date']
                end_date = form.cleaned_data['end_date']

                if end_date > start_date:
                    details = form.save(commit=False)
                    details.leave_status = Leave_status
                    details.user_id=userid
                    details.date_of_application=Date_of_application
                    details.save()  
                    messages.success(request,"leave application form submmited sucessfully")
                else:
                    messages.error(request,"leave application submission failed end date less than start date")

        except:
            messages.error(request,"leave application submission failed")


    form = leaveForm(request.POST)
    # levty=LeaveType.objects.all()
    return render(request,'leaveapplication.html',{'form':form})


def leaveStructure(request):
    userid = request.session['user_id']
    levaveStructure = Leaves.objects.filter(user=userid)
    employee = Employee.objects.filter(user=userid)
    employeeDetails = EmployeeDetails.objects.filter(user=userid)
    levaveApplicationDetails=LeaveApplication.objects.filter(user=userid)
    

    context={
    'levaveStructure':levaveStructure,
    'employee':employee,
    'employeeDetails':employeeDetails,
    'levaveApplicationDetails':levaveApplicationDetails
    }

   
    return render(request,'leaveStructure.html',context)

def leaveStatus(request):
    userid = request.session['user_id']
    levaveApplicationDetails = LeaveApplication.objects.filter(user=userid)

    context={
        'levaveApplicationDetails' :levaveApplicationDetails,
    }

    return render(request,'leavestatus.html',context)