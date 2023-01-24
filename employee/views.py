from django.shortcuts import render

# Create your views here.
import datetime
from django.shortcuts import render, redirect
import mysql.connector as sql
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from login.models import *
from login.models import *
from employee.forms import *



def employee(request):
    return render(request, 'employee_home.html')


def profile(request):
    
    userid = name = request.session['user_id']
    emp = Employee.objects.filter(user=userid) 
    print(emp)
    context={'emp':emp}
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
    levstr = Leaves.objects.filter(user=userid)
    emp = Employee.objects.filter(user=userid)
    empdet = EmployeeDetails.objects.filter(user=userid)
    levfor=LeaveApplication.objects.filter(user=userid)
    

    context={
    'levstr':levstr,
    'emp':emp,
    'empdet':empdet,
    'levfor':levfor
    }

   
    return render(request,'leaveStructure.html',context)

def leaveStatus(request):
    userid = request.session['user_id']
    levfor = LeaveApplication.objects.filter(user=userid)

    context={
        'levfor' :levfor,
    }

    return render(request,'leavestatus.html',context)