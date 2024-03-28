from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Account, Category, Transaction
from .forms import AccountForm

def home(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}")
    
    context = {'user': request.user}
    
    accounts = Account.objects.filter(user=request.user)
    if not accounts:
        messages.info(request, 'Você não possui nenhuma conta cadastrada!')
    else:
        context.update({'accounts': accounts})
        selected_account_id = request.GET.get('account')
        
        if selected_account_id:
            selected_account = accounts.get(account_id=selected_account_id)
        else:
            selected_account = accounts.first()
            
        context.update({'selected_account': selected_account})
        
        transactions = Transaction.objects.filter(account=selected_account)
        context.update({'transactions': transactions})
    
    return render(request, 'home.html', context=context)

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

def newaccount_view(request: HttpRequest):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.info(request, 'Conta criada com sucesso!')
            return redirect('home')  # Redireciona para alguma view após o sucesso do formulário
    else:
        form = AccountForm()
        
    return render(request, 'newaccount.html', {'form': form})