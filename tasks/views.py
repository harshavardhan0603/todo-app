from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout


# from matplotlib import pyplot as plt
# import numpy as np
 
 
# Creating dataset




def index(request):
    if request.user.is_authenticated:
        tasks = Task.objects.all().filter(user=request.user)
        if request.method == "POST":
            task = Task( title= request.POST["title"], user = request.user)
            task.save()

        n = 0
        for i in tasks:
            if not i.complete:
                n +=1
        context = {"task":tasks ,"count": n }
        return render(request,"list.html", context)
    
    else :
        
        return redirect("register/")


def update(request, n):
    task = Task.objects.get(id = n)
    forms = Taskform(instance=task)
    if request.method == "POST":
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    # a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11,20, 51, 5, 79, 31,27])


    # fig, ax = plt.subplots(figsize =(10, 7))
    # ax.hist(a, bins = [0, 25, 50, 75, 100])
 

    # x= plt.show()
    return render(request,"update.html",{"forms":forms })


def deleteTask(request,n):
    task = Task.objects.get(id = n)
    task.delete()
    return redirect("/")

def registerpage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password1']
        confirm_password=request.POST['password2']
        if password==confirm_password:
            try:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                user = authenticate(username=username,password=password)
                login(request,user)
                return redirect('/')
            except Exception as e:
                return redirect('/')
        else:
            return redirect('/')
    else:
         return render(request,"register.html")


def log_in(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return redirect("register/")
    return render(request, "login.html")

def log_out(request):
    logout(request)
    return redirect("register/")


# Create your views here.
