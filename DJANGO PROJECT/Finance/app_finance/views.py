from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpRequest

def home(request):
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}")
    
    return render(request, 'home.html')

def login(request: HttpRequest):
    return render(request, 'login.html')
