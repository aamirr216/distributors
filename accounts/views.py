from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def register(request):
    if not request.user.is_authenticated:            
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']
            context = {
                'first_name': first_name,
                'last_name': last_name,
                'username': username,
                'email': email
            }
            if password == password2:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username is Taken')
                    # return redirect('register')
                    return render(request, 'accounts/register.html', context)
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'Eamil already being used')
                        # return redirect('register')
                        return render(request, 'accounts/register.html', context)
                    else:
                        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,email=email,password=password)
                        user.save()
                        messages.success(request, 'You are now registered and can log in')                    
                        # return redirect('login')
                        return render(request, 'accounts/login.html', context)            
            else:
                messages.error(request,'password do not match')
                return render(request, 'accounts/register.html', context)    
        else:
            return render(request, 'accounts/register.html')
    else:
        messages.error(request,'Already LoggedIn')
        return redirect('dashboard')

def login(request):    
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)      
                messages.success(request, 'You are now logged in')        
                return redirect('orders')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')
        else:
            return render(request, 'accounts/login.html')
    else:
        messages.error(request,'Already LoggedIn')
        return redirect('orders')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')