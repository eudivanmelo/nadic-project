# Generated by Django 5.0.2 on 2024-03-27 22:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('Expense', 'Expense'), ('Revenue', 'Revenue')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=16)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=16)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_finance.account')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_finance.category')),
            ],
        ),
    ]
