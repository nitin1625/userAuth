from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from .middlewares import * 

# request -> This argument is required and represents 
# the incoming HTTP request. It contains information 
# about the user’s request, such as headers, method, 
# and any data submitted via forms.

@guest
def register_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('login')
    else :
            initial_data={'username':'','password1':'','password2':''}
            form=UserCreationForm(initial=initial_data)
    return render(request,'register.html',{'form':form})  # return HTTP Response

@guest
def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
    else :
            initial_data={'username':'','password':''}
            form=AuthenticationForm(initial=initial_data)
    return render(request,'login.html',{'form':form})  # return HTTP Response



def logout_view(request):
    logout(request)
    return redirect('login')

@auth
def home_view(request):
    return render(request,'home.html')



        





