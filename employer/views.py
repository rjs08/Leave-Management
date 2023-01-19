from django.shortcuts import render

# Create your views here.
import datetime
from django.shortcuts import render, redirect
import mysql.connector as sql
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from login.models import *


def employer(request):
    return render(request, 'employer_home.html')


def profileadmin(request):
    userid = request.session['user_id']
    emp = Employee.objects.filter(user=userid) 
    context={'emp':emp}
    return render(request,'profileadmin.html',context)


def createemp(request):
    return render(request,'createemp.html')

def saveemp(request):
    userid=request.session['user_id']
 
        #AppUser table
    username = request.POST["username"]
    password = request.POST["password"]
    access_label = request.POST["access_label"]
    appUser = AppUser(username=username,password=password,access_label=access_label)
    appUser.save()
    
        #Employee table
    user = appUser.user_id
    print(user)
    firstname = request.POST["firstname"]
    lastname = request.POST["lastname"]
    age = request.POST["age"]
    gender = request.POST["gender"]
    email = request.POST["email"]
    contact = request.POST["contact"]
    employee = Employee(firstname=firstname,lastname=lastname,age=age,gender=gender,email=email,contact=contact,user_id=user)
    employee.save()



    date_of_join = request.POST["date_of_join"]
    project = request.POST["project"]
    employeeDetails = EmployeeDetails(date_of_join=date_of_join,project=project,user_id=user)
    employeeDetails.save()



    messages.info(request,"emp registered")
    return HttpResponse('emp registered')

def updateemp(request):
    return render(request, 'empupdate.html')

def empleaves(request):
    return render(request, 'emp_applied_leaves.html')

def leaves_structure(request):
    return render(request, 'emp_leaves_structure.html')


def emp_details(request):
    emps=Employee.objects.all()
    empsd=EmployeeDetails.objects.all()
    context={'emps':emps,'empsd':empsd}

    return render(request, 'emp_details.html',context=context)