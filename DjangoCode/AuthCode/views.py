from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

            # Sign up Function
def Signup(request):
             # Taking the data from Signup Page
    if request.method == 'POST':
        uname = request.POST.get('username')
        f_name = request.POST.get('full_name')
        email = request.POST.get('email')
        upass = request.POST.get('password')

                # authenticating data to create user
        user = User.objects.create_user(username=uname, email=email, password=upass, first_name=f_name)
        user.save()

        if user != None:
            return redirect('Login')
    else:
        return render(request, 'signup.html')

            
            # Login Function
def Login(request):
    # If user is logged in then simply go to profile  else go inside the if condition
    if not request.user.is_authenticated:
        if request.method == 'POST':
                 # Taking data from html page
            uname = request.POST.get('username')
            upass = request.POST.get('password')
                # Authenticating  if the username and password is correct
            user = authenticate(username=uname, password=upass)
            if user != None:
                login(request, user)
                return redirect('Profile')
            else:
                return redirect('Login')

        else:
            return render(request, 'login.html')

    else:
         return redirect('Profile')

            # Profile Function
def Profile(request):
         # If user is logged in then show profile screen else show login screen
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
         return redirect('Login')

        # Logout Function
def Logout(request):
     logout(request)
     return redirect('Login')
    #  Simply logout and redirecting to Login Function
