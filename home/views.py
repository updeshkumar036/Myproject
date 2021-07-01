from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request):
    return render(request,'index.html')

def exercises(request):
    return render(request,'exercises.html')

def nutrition(request):
    return render(request,'nutrition.html')

def workout(request):
    return render(request,'workout.html')

def customize(request):
    return render(request,'customize.html')



def handleSignup(request):
    if request.method == "POST":
        firstname=request.POST["firstname" ]
        lastname=request.POST["lastname"]
        username=request.POST["username" ]
        email=request.POST["email" ]
        password=request.POST["password" ]
        password2=request.POST["password2"]
        
        #check for erreos,
        if len(username)>10:
            messages.error(request,"username must be under 10 char")
            return redirect("/")
        if not username.isalnum():
            messages.error(request,"username should only contain letters and numbers ")
            return redirect("/")
        if password != password2:
            messages.error(request,"Password do not match")
            return redirect("/")
           

        #create user
        myuser=User.objects.create_user(username=username, email=email, password=password)
        myuser.firstname=firstname 
        myuser.lastname=lastname
        myuser.save()
        messages.success(request,"Your account has been succesfully created")
        return redirect("home")

       
    else:
        return HttpResponse("404-Not Found")

def handleLogin(request):
    if request.method=="POST":
        loginusername=request.POST["loginusername"]
        loginpass=request.POST["loginpass"]
        user= authenticate(username=loginusername,password=loginpass)
        
        if user is not None:
            login(request,user)
            messages.success(request,"successfully logged in ")
            return redirect("/")
        else:
            messages.error(request,"chala ja bhosdike signup krke aa wrna bhut peluga")
            return redirect("/")
    
    return HttpResponse("404-Not Found")

def handleLogout(request):
    
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
    
    return HttpResponse('handleLogout')



