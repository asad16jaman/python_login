from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.forms import User,UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
class LoginFunc(View):

    def get(self,request):

        if request.user.is_authenticated:
            return render(request, 'index.html')
        else:
            loginform=AuthenticationForm()
            return render(request,'login.html',{'form':loginform})

    def post(self,request):
        name=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=name , password=password)

        if user is None:
            messages.info(request,'inter valid account ------ ')
            return redirect('/')
        else:
            login(request,user)
            context={
                'is_super':request.user.is_superuser
            }
            return render(request,'index.html' ,{'data':context})

class LogoutFunc(View):
    def get(self,request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('/')

class CreationFunc(View):

    def get(self,request):
        form=UserCreationForm()
        return render(request,'registration.html',{'form':form})

    def post(self,request):
        profile=UserCreationForm(request.POST)
        if profile.is_valid():
            profile.save()
            messages.info(request,'registration successfully -----------')
            return redirect('/')
        else:
            messages.info(request,'inter valid information ')
            return redirect('/')
