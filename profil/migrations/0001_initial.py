# Generated by Django 4.1.7 on 2023-03-20 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilModel',
            fields=[
                ('nom', models.CharField(max_length=200, null=True)),
                ('prenom', models.CharField(max_length=200, null=True)),
                ('telephone', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('profession', models.CharField(max_length=200, null=True)),
                ('pays', models.CharField(max_length=100, null=True)),
                ('departement', models.CharField(max_length=100, null=True)),
                ('commune', models.CharField(max_length=200, null=True)),
                ('quartier', models.CharField(max_length=200, null=True)),
                ('created_date', models.DateField(auto_now=True)),
                ('avatar', models.CharField(max_length=10000, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]