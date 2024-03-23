from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout

def home(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}")
    
    return render(request, 'home.html', context={'user': request.user})

def login_view(request: HttpRequest):
    """
    Exibe a página de login e autentica o usuário.

    Args:
        request (HttpRequest): O objeto de solicitação HTTP.

    Returns:
        HttpResponse: A resposta HTTP renderizada para a página de login.
    """
    # Verifica se o usuário já está autenticado e redireciona para a página inicial
    if request.user.is_authenticated:
        return redirect("home")
    
    # Se o método da solicitação for POST, tenta autenticar o usuário
    if request.method == 'POST':
        # Obtém as credenciais do formulário de login
        username = request.POST['username']
        password = request.POST['password']
        
        # Autentica o usuário com as credenciais fornecidas
        user = authenticate(request, username=username, password=password)
        
        # Se o usuário for autenticado com sucesso, realiza o login e redireciona para a página inicial
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Se as credenciais forem inválidas, exibe uma mensagem de erro
            error_message = "Credenciais inválidas. Por favor, tente novamente."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        # Se a solicitação não for do tipo POST, exibe a página de login
        return render(request, 'login.html')

def logout_view(request: HttpRequest):
    logout(request)
    # Redireciona o usuário para a página de login após o logout
    return redirect('login')