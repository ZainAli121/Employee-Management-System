from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.
def registerUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login')
    else:
        return render(request, 'users/login.html')


def loginUser(request):
    page = 'login'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username=username)
        user = authenticate(request=request, username=username, password=password)
        if user is not None and user.is_employee and not user.is_admin:
            login(request, user)
            return redirect('employees_site')
        elif user is not None and user.is_admin:
            login(request, user)
            return redirect('admin_site')
        else:
            return render(request, 'users/login.html')
        
    context = {'page': page}
    return render(request, 'users/login.html', context)
    
def logoutUser(request):
    logout(request)
    return render(request, 'users/login.html')