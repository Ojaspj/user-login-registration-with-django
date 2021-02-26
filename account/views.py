from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.warning(request, 'Invalid credentials. Enter valid username or password !')
            return redirect('login')

    else:
        return render(request,'login.html')    

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request,'The username you'"'re looking for is already being used by someone. Please, use another one.")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.warning(request,'Email already exist. Please, use another one.')
                return redirect('register')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.success(request,'Your account succesfully registered. SignIn Now!')
                return redirect('login')

        else:
            messages.warning(request,'Password not matching..Try again.')    
            return redirect('register')
        return redirect('login')
        
    else:
        return render(request,'register.html')



def logout(request):
    auth.logout(request)
    return redirect('login')      

def home(request):
    return render(request, 'home.html') 