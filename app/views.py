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
    print(username)
    m=sql.connect(host="localhost",user="root",passwd="root",database='project2')
    cursor=m.cursor()
    query="select * from app_appuser where username='{}' and password='{}' ".format(username,password)
    cursor.execute(query)
    found=cursor.fetchall()    
    
    if(found):
        request.session['user_id']=-1
        #print(request.session['user_id'])
        request.session['user_id']=found[0][0]
        #d={'username':username}
        #print("app user id",found[0][0])     to see on console which user login
        #return render(request,'emphome.html')
        return HttpResponseRedirect('/abc',request)
    else:
        messages.info(request,"wrong credentials")
        return HttpResponseRedirect('/')


def abc(request):
   
    userid = request.session['user_id']
    
    m=sql.connect(host="localhost",user="root",passwd="root",database='project2')
    cursor=m.cursor()
    query="select access_label from app_appuser where user_id={}".format(userid)
    print(query)
    cursor.execute(query)
    found=cursor.fetchall() 
    ind=found[0][0]
    print(ind)
    if ind==1:
        return HttpResponseRedirect('/employee',request)
    else:
        return HttpResponseRedirect('/adminn',request)

def admin(request):
    return render(request,'adminhome.html')

def employee(request):
    return render(request,'emphome.html')

def logout(request):
    try:
        del request.session['user_id']
    except:
        return redirect('/')
    return redirect('/')

def profile(request):
    
    userid = request.session['user_id']
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

#starts from hear

def leaveApplication(request):
    if request.POST:
        Date_of_application = request.POST["Date_of_application"]
        Start_date = request.POST["Start_date"]
        End_date = request.POST["End_date"]
        Leave_discription = request.POST["Leave_discription"]
        Leave_type = request.POST["Leave_type"]

        Leave_status='pending'
        userid = request.session['user_id']
        
        try:
            leaveApplication = LeaveApplication(date_of_application=Date_of_application,start_date=Start_date,end_date=End_date,leave_status=Leave_status,user_id=userid,leave_description=Leave_discription,leave_type=Leave_type)
            leaveApplication.save()
            messages.success(request,"leave application form submmited sucessfully")
        except:
            messages.error(request,"leave application submission failed")
        

    return render(request,'leaveapplication.html')


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



