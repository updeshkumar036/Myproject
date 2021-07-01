from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("",views.index,name="home"),
    path("exercises",views.exercises,name="exercises"),
    path("nutrition",views.nutrition,name="nutrition"),
    path("workout",views.workout,name="workout"),
    path("customize",views.customize,name="customize"),
    path("signup",views.handleSignup,name="handleSignup"),
    path("login",views.handleLogin,name="handleLogin"),
    path("logout",views.handleLogout,name="handleLogout")
    
    
    
]