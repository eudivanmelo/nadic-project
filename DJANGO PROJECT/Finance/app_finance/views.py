from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.contrib.auth import authenticate, login

def home(request):
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}")
    
    return render(request, 'home.html')

def login_view(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirecione para a página de sucesso ou para qualquer página que desejar
            return redirect('home')
        else:
            error_message = "Credenciais inválidas. Por favor, tente novamente."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
