from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    """
    Representa uma conta de usuário.

    Atributos:
        account_id (AutoField): Campo de chave primária autoincrementável que identifica exclusivamente cada conta.
        user (ForeignKey): Chave estrangeira que relaciona a conta com um usuário específico. Cada conta está associada a um usuário.
        name (CharField): Nome da conta.
        balance (DecimalField): Saldo da conta.

    Métodos:
        __str__: Retorna uma representação em string da conta contendo o nome da conta e o usuário.
    """

    account_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=16, decimal_places=2)

    def __str__(self) -> str:
        """
        Retorna uma representação em string da conta.

        Retorna:
            str: Uma representação em string da conta contendo o nome da conta e o usuário.
        """
        return f"{self.name} por: {self.user}"

class Category(models.Model):
    """
    Representa uma categoria para classificar transações financeiras.

    Atributos:
        category_id (AutoField): Campo de chave primária autoincrementável que identifica exclusivamente cada categoria.
        name (CharField): Nome da categoria.
        type (CharField): Tipo da categoria, pode ser 'Expense' (despesa) ou 'Revenue' (receita).

    Métodos:
        __str__: Retorna uma representação em string da categoria contendo apenas o nome da categoria.
    """

    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    TYPE_CHOICES = (
        ('Expense', 'Expense'),
        ('Revenue', 'Revenue'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self) -> str:
        """
        Retorna uma representação em string da categoria.

        Retorna:
            str: O nome da categoria.
        """
        return f"{self.name}"

class Transaction(models.Model):
    """
    Representa uma transação financeira.

    Atributos:
        transaction_id (AutoField): Campo de chave primária autoincrementável que identifica exclusivamente cada transação.
        account (ForeignKey): Chave estrangeira que relaciona a transação com uma conta específica. Cada transação está associada a uma conta.
        category (ForeignKey): Chave estrangeira que relaciona a transação com uma categoria específica. Cada transação está associada a uma categoria.
        date (DateField): Data da transação.
        value (DecimalField): Valor da transação.
        name (CharField): Nome ou descrição da transação.

    Métodos:
        __str__: Retorna uma representação em string da transação contendo o nome da transação, o nome da conta e o usuário da conta.
    """

    transaction_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.DecimalField(max_digits=16, decimal_places=2)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        """
        Retorna uma representação em string da transação.

        Retorna:
            str: Uma representação em string da transação contendo o nome da transação, o nome da conta e o usuário da conta.
        """
        return f"{self.name} em {self.account.name} por: {self.account.user}"
    
    def save(self, *args, **kwargs):
        """
        Sobrescreve o método save() para atualizar o saldo da conta após salvar a transação.
        """
        super().save(*args, **kwargs)  # Chama o método save() original para salvar a transação

        # Verifica o tipo de categoria associada à transação
        if self.category.type == 'Revenue':
            # Se for uma receita, adiciona o valor da transação ao saldo da conta
            self.account.balance += self.value
        elif self.category.type == 'Expense':
            # Se for uma despesa, subtrai o valor da transação do saldo da conta
            self.account.balance -= self.value
        
        # Salva a conta com o novo saldo
        self.account.save()
