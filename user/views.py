from django.shortcuts import render
from .models import CourseDetails
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import redirect
from .forms import *
# Create your views here.

# def homepage(request):
#     context={}
#     course_details=CourseDetails.objects.all()
    
#     return render(request,'user/index.html',{})

class Homepage(ListView):
    context={}
    model=CourseDetails
    template_name = "user/index.html"
    context_object_name ='course_list'
    

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("save--------")
            messages.success(request, 'User registered successfully')
            return redirect('/login/')
        else:
            messages.error(request, 'Invalid form data')
    else:
        form = RegistrationForm()
    
    return render(request, 'user/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')  # Replace 'home' with the URL name of your home page
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = UserLoginForm()

    return render(request, 'user/login.html', {'form': form})

# def login(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('/dashboard/')
#         else:
#             messages.error(request,'Invalid Credential')
#             return redirect('/login/')
#     return render(request,"user/login.html",{})

def logout(request):
    auth.logout(request)
    return redirect("/")