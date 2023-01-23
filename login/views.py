from django.shortcuts import render

# Create your views here.
import datetime
from django.shortcuts import render, redirect
import mysql.connector as sql
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from login.models import *


# Create your views here.

def login(request):
    return render(request, 'login.html')


def select(request):
    username = request.POST["username"]
    password = request.POST["password"]
    print(username)
    print(password)
    m = sql.connect(host="localhost", user="root", passwd="root", database='project1')
    cursor = m.cursor()
    query = "select * from login_appuser where username='{}' and password='{}' ".format(username, password)
    cursor.execute(query)
    found = cursor.fetchall()

    if found:
        userid = found[0][0]
        access_label = found[0][3]
        print(access_label)
        request.session['user_id'] = userid

        if access_label == 1:
            return HttpResponseRedirect('/employee', request)
        else:
            return HttpResponseRedirect('/employer', request)
    else:
        messages.info(request, "wrong credentials")
        return HttpResponseRedirect('/appUser')

def logout(request):
    try:
        del request.session['user_id']
    except:
        return redirect('/appUser')
    return redirect('/appUser')

