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


# This function is for validate user credentials and depending on access label redirect to home page
def select(request):
    username = request.POST["username"]
    password = request.POST["password"]

    try:
        user = AppUser.objects.filter(username=username, password=password).values()
        if user:
            userid = user[0]['user_id']
            access_label = user[0]['access_label']
            request.session['user_id'] = userid

            if access_label == 1:
                return HttpResponseRedirect('/employee', request)
            else:
                return HttpResponseRedirect('/employer', request)
        else:
            messages.info(request, "wrong credentials")
            return HttpResponseRedirect('/appUser')
    except Exception as e:
        messages.error(request, "An error occurred while logging in: " + str(e))
        return HttpResponseRedirect('/appUser')


def logout(request):
    try:
        del request.session['user_id']
    except:
        return redirect('/appUser')
    return redirect('/appUser')
