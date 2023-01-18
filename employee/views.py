import datetime
from django.shortcuts import render, redirect
import mysql.connector as sql
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from login.models import *
# from app.models import *




def employee(request):
    return render(request, 'employee_home.html')


def profile(request):
    
    userid = request.session['user_id']
    emp = Employee.objects.filter(user=userid) 
    print(emp)
    context={'emp':emp}
    return render(request,'profile.html',context)


def leaveApplication(request):
    
    if request.POST:
        # Date_of_application = request.POST["Date_of_application"]
        try:
            Date_of_application = datetime.datetime.now()
            Start_date = request.POST["Start_date"]
            End_date = request.POST["End_date"]
            Leave_discription = request.POST["Leave_discription"]
            Leave_type = request.POST["Leave_type"]
            
            mydata = LeaveType.objects.filter(leave_type=Leave_type)
            leave_type_id=mydata[0].leave_type_id

            Leave_status='pending'
            userid = request.session['user_id']
        
            if End_date > Start_date:
                leaveApplication = LeaveApplication(date_of_application=Date_of_application,start_date=Start_date,end_date=End_date,leave_status=Leave_status,user_id=userid,leave_description=Leave_discription,leave_type_id=leave_type_id)
                leaveApplication.save()
                messages.success(request,"leave application form submmited sucessfully")
            else:
              messages.error(request,"leave application submission failed")  

              
        except:
            messages.error(request,"leave application submission failed")
        
    levty=LeaveType.objects.all()
    return render(request,'leaveapplication.html',{'levty':levty})


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

