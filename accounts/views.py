from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Safe handling - filter and first
        user = User.objects.filter(email=email).first()
        
        if user:
            auth_user = authenticate(request, username=user.username, password=password)
            if auth_user:
                auth_login(request, auth_user)
                return redirect('home')  # Or redirect to a dashboard
            else:
                messages.error(request, "Invalid password")
        else:
            messages.error(request, "Email not found")
        return redirect('login')
    
    return render(request, 'index.html')



@csrf_exempt
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check for duplicate email
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken")
            return redirect('register')
        
        # Use email as username too
        user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
        user.save()
        messages.success(request, "Registration successful")
        return redirect('login')
    
    return render(request, 'register.html')


@csrf_exempt
def logout(request):
    auth_logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')


@csrf_exempt
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # lowercase 'username'
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            auth_login(request, user)
            return redirect('upload_book')  # URL name, NOT template
        else:
            messages.error(request, 'Invalid credentials or not authorized.')
            return redirect('admin_login')  # Redirect to login page on failure

    return render(request, 'admin_login.html')