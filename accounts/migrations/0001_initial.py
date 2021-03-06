# Generated by Django 2.1.3 on 2018-12-06 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome do bairro')),
                ('slug', models.SlugField(max_length=150, verbose_name='Identificador')),
            ],
            options={
                'verbose_name': 'Bairro',
                'verbose_name_plural': 'Bairros',
            },
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome da cidade')),
                ('slug', models.SlugField(max_length=150, verbose_name='Identificador')),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nome do cliente')),
                ('slug', models.SlugField(max_length=150, verbose_name='Identificador')),
                ('cliente_sobrnome', models.CharField(max_length=150, verbose_name='Sobrnome')),
                ('cliente_data_nascimento', models.DateField(verbose_name='Data')),
                ('cliente_estado_civil', models.CharField(max_length=150, verbose_name='Estado civil')),
                ('cliente_email', models.EmailField(max_length=150, verbose_name='Email')),
                ('cliente_phone_fixo', models.CharField(max_length=50, verbose_name='Telefone fixo')),
                ('cliente_cel_phone', models.CharField(max_length=50, verbose_name='Celular')),
                ('cliente_cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Dados_cartao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Cartão')),
                ('slug', models.SlugField(max_length=150, verbose_name='Identificador')),
                ('cartao_numero', models.CharField(max_length=50, verbose_name='Número')),
                ('cartao_data', models.DateField(verbose_name='Vencimento em')),
                ('cartao_security_cod', models.CharField(max_length=10, verbose_name='Código de segurança')),
                ('cartao_password', models.CharField(max_length=150, verbose_name='Senha')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Dados do cartao',
                'verbose_name_plural': 'Dados dos cartões',
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Login')),
                ('slug', models.SlugField(max_length=150, verbose_name='Identificador')),
                ('login_password', models.CharField(max_length=150, verbose_name='Password')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Cliente', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Login',
                'verbose_name_plural': 'Logins',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome do país')),
                ('slug', models.SlugField(max_length=150, verbose_name='Identificador')),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Países',
            },
        ),
        migrations.CreateModel(
            name='Pessoa_juridica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
                ('slug', models.SlugField(max_length=150, verbose_name='Identificador')),
                ('pj_razao_social', models.CharField(max_length=150, verbose_name='Razão social')),
                ('pj_cnpj', models.CharField(max_length=14, verbose_name='CNPJ')),
                ('pj_insc_estadual', models.CharField(max_length=20, verbose_name='Inscrição estadul')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Cliente', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Pessoa juridica',
                'verbose_name_plural': 'Pessoas juridicas',
            },
        ),
        migrations.CreateModel(
            name='Rua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nome da rua')),
                ('slug', models.SlugField(max_length=150, verbose_name='Identificador')),
                ('rua_numero', models.CharField(max_length=10, verbose_name='Número')),
                ('rua_complemento', models.CharField(max_length=150, verbose_name='Complemento')),
                ('rua_cep', models.CharField(max_length=50, verbose_name='CEP')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('bairro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Bairro', verbose_name='Bairro')),
            ],
            options={
                'verbose_name': 'Rua',
                'verbose_name_plural': 'Ruas',
            },
        ),
        migrations.CreateModel(
            name='Uf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome do  estado')),
                ('slug', models.SlugField(max_length=150, verbose_name='Identificador')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Pais', verbose_name='País')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.AddField(
            model_name='dados_cartao',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Pais', verbose_name='País'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='rua',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Rua', verbose_name='Rua'),
        ),
        migrations.AddField(
            model_name='cidade',
            name='uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Uf', verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='bairro',
            name='cidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Cidade', verbose_name='Cidade'),
        ),
    ]
