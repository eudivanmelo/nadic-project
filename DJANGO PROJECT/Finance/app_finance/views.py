from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Account, Category, Transaction
from .forms import AccountForm, TransctionForm, CategoryForm

def get_defaultcontext(request: HttpRequest):
    """
    Obtém o contexto padrão para renderização de páginas.

    Este método é utilizado para criar um contexto padrão que inclui o usuário atual e suas contas associadas.

    Parâmetros:
        request (HttpRequest): O objeto de requisição HTTP.

    Retorna:
        dict: Um dicionário contendo o contexto padrão com o usuário atual e suas contas associadas.
    """
    # Inicializa o contexto com o usuário atual
    context = {'user': request.user}

    # Obtém as contas associadas ao usuário atual
    accounts = Account.objects.filter(user=request.user)

    # Verifica se o usuário possui contas
    if not accounts:
        messages.info(request, 'Você não possui nenhuma conta cadastrada!')
    else:
        # Adiciona as contas ao contexto
        context.update({'accounts': accounts})

        # Obtém o ID da conta selecionada (se houver)
        selected_account_id = request.GET.get('account')

        if selected_account_id:
            # Verifica se a conta selecionada existe nas contas do usuário
            if accounts.filter(account_id=selected_account_id):
                selected_account = accounts.get(account_id=selected_account_id)
            else:
                # Seleciona a primeira conta por padrão
                selected_account = accounts.first()
        else:
            # Seleciona a primeira conta por padrão
            selected_account = accounts.first()
        
        # Adiciona a conta selecionada ao contexto
        context.update({'selected_account': selected_account})
    
    return context

def home(request: HttpRequest):
    """
    Renderiza a página inicial do usuário.

    Parâmetros:
        request (HttpRequest): O objeto de requisição HTTP.

    Retorna:
        HttpResponse: Renderiza a página 'home.html' com os detalhes do usuário, contas e transações associadas.
                      Redireciona para a página de login se o usuário não estiver autenticado.
    """
    # Redireciona para a página de login se o usuário não estiver autenticado
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}")

    # Obtém o contexto padrão
    context = get_defaultcontext(request)

    # Verifica se uma conta está selecionada
    if context['selected_account']:
        # Obtém as transações associadas à conta selecionada
        transactions = Transaction.objects.filter(account=context['selected_account'])

        # Adiciona as transações ao contexto
        context.update({'transactions': transactions})

    # Renderiza a página inicial com o contexto atualizado
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
    """
    Realiza o logout de um usuário.

    Parâmetros:
        request (HttpRequest): O objeto de requisição HTTP.

    Retorna:
        HttpResponseRedirect: Redireciona o usuário para a página de login após o logout.
    """
    logout(request)
    # Redireciona o usuário para a página de login após o logout
    return redirect('login')

def newaccount_view(request: HttpRequest):
    """
    Cria uma nova conta para o usuário atual.

    Parâmetros:
        request (HttpRequest): O objeto de requisição HTTP.

    Retorna:
        HttpResponse: Renderiza a página 'newaccount.html' se o método de requisição for GET.
                      Redireciona para a página inicial ('home') se o método de requisição for POST e o formulário for válido.
    """
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            # Define o usuário atual como o proprietário da conta antes de salvar
            form.instance.user = request.user
            form.save()
            messages.info(request, 'Conta criada com sucesso!')  # exibe uma mensagem de sucesso
            return redirect('home')  # redireciona o usuário para a página inicial após a criação da conta
    
    # Obtém o contexto padrão
    context = get_defaultcontext(request)
    
    # Renderiza a página para criar uma nova conta
    return render(request, 'newaccount.html', context)

def addtransaction_view(request: HttpRequest):
    # Obtém o contexto padrão
    context = get_defaultcontext(request)
    
    # Obter categorias
    context.update({'categorys': Category.objects.all()})
    
    if request.method == 'POST':
        transaction_form = TransctionForm(request.POST)
        if transaction_form.is_valid():
            transaction_form.save()
            return redirect(reverse('home') + f"?account={context['selected_account'].account_id}")  # redireciona o usuário para a página inicial após a criação da conta
        
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return render(request, 'addtransaction.html', context)
    else:
        transaction_form = TransctionForm()
    
    return render(request, 'addtransaction.html', context)