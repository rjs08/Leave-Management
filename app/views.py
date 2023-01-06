from django.shortcuts import render,redirect
import mysql.connector as sql
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from app.models import *

# Create your views here.

def login(request):
    return render(request, 'login.html')


def emphome(request):
 
    username = request.POST["username"]
    password = request.POST["password"]

    m=sql.connect(host="localhost",user="root",passwd="root",database='project1')
    cursor=m.cursor()
    query="select * from app_appuser where username='{}' and password='{}' ".format(username,password)
    cursor.execute(query)
    found=cursor.fetchall()    
    
    if(found):
        userid=found[0][0]
        access_label=found[0][3]

        request.session['user_id']=userid

        if access_label==1:
            return HttpResponseRedirect('/employee',request)
        else:
            return HttpResponseRedirect('/home',request)
    else:
        messages.info(request,"wrong credentials")
        return HttpResponseRedirect('/appUser')

def admin(request):
    return render(request,'adminhome.html')

def employee(request):
    return render(request,'emphome.html')

def logout(request):
    try:
        del request.session['user_id']
    except:
        return redirect('/appUser')
    return redirect('/appUser')

def profile(request):
    
    userid = name = request.session['user_id']
    emp = Employee.objects.filter(user=userid) 
    print(emp)
    context={'emp':emp}
    return render(request,'profile.html',context)

def profileadmin(request):
    userid = request.session['user_id']
    emp = Employee.objects.filter(user=userid) 
    print(emp)
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