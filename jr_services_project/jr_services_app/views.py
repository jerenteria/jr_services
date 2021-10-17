from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *

def index(request):
    return render(request, "index.html")

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request, "home.html")

def register(request):
    if request.method=='POST':
        # validate the data
        errors=User.objects.validator(request.POST)
        if errors:
            for error in errors:
                messages.error(request, errors[error])
            return redirect("/")
        ## encrypting our password
        ## store plaintext password in variable
        user_pw=request.POST['pw']
        ## hash the password
        hash_pw=bcrypt.hashpw(user_pw.encode(), bcrypt.gensalt()).decode()
        #test
        print(hash_pw)
        new_user=User.objects.create(first_name=request.POST['f_n'], last_name=request.POST['l_n'], email=request.POST['email'], password=hash_pw)
        print(new_user)
        request.session['user_id']=new_user.id
        request.session['user_name']=f"{new_user.first_name} {new_user.last_name}"
        return redirect('/home')
    return redirect('/')

def aboutus(request):
    return render(request, "aboutus.html")


def login(request):
    ## loging a user in
    if request.method=='POST':
        ## query for logged user
        logged_user=User.objects.filter(email=request.POST['email'])
        if logged_user:
            logged_user=logged_user[0]
            ## compare the passwords
            if bcrypt.checkpw(request.POST['pw'].encode(), logged_user.password.encode()):
                request.session['user_id']=logged_user.id
                request.session['user_name']=f"{logged_user.first_name} {logged_user.last_name}"
                return redirect('/home')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def makePayment(request):
    return redirect('/makePayment')
