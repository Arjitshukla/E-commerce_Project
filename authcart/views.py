from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages 
from django.contrib.auth  import authenticate,login,logout


# Create your views here.

def  signup(request):
    if request.method=="POST":
            # Get the post parameters
        # name = request.POST['name']
        email = request.POST['email']
        Userpass1 = request.POST['pass1']
        Userpass2 = request.POST['pass2']
        # check for errorneous input
        if  Userpass1 != Userpass2 :
            messages.warning(request,'Passwords do not matched')
            return render(request,"signup.html")
         
        try:
            if User.objects.get(username=email):
                 messages.info(request,'Enter your Email and password')
                 return redirect('/auth/login')
 
        except Exception  as identifier :
            pass
        # Create the user
        user = User.objects.create_user(email,email, Userpass1)
        user.save()
        messages.success(request, " User able to login⤵️")
        return redirect('/auth/login')

    return render(request,"signup.html")
     
def  handlelogin(request):
    if request.method=="POST":
        
        username  = request.POST['email']
        userpassword =request.POST['pass1']
        myuser = authenticate(username=username,password= userpassword )

        if myuser is not None:
            login(request,myuser)
            # messages.success (request,"Login Success")
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials ')
            return redirect('/auth/login')
    return render(request,"login.html")

def  handlelogout(request):  
     logout(request)
     messages.info(request,"Successfully logged out 😊")
     return redirect('/auth/login')
   

