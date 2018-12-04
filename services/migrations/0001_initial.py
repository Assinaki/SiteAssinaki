# Generated by Django 2.1.3 on 2018-12-04 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assinatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assinatura_cod', models.CharField(max_length=11, verbose_name='Assinatura')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Cliente')),
            ],
            options={
                'verbose_name': 'Assinatura',
                'verbose_name_plural': 'Assinaturas',
            },
        ),
        migrations.CreateModel(
            name='Dados_cartao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartao_nome', models.CharField(max_length=150, verbose_name='Cartão')),
                ('cartao_numero', models.CharField(max_length=50, verbose_name='Número')),
                ('cartao_data', models.DateField(verbose_name='Vencimento em')),
                ('cartao_security_cod', models.CharField(max_length=10, verbose_name='Código de segurança')),
                ('cartao_password', models.CharField(max_length=150, verbose_name='Senha')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Pais')),
            ],
            options={
                'verbose_name': 'Dados do cartao',
                'verbose_name_plural': 'Dados dos cartões',
            },
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento_content', models.CharField(max_length=150, verbose_name='Documento')),
                ('documento_data', models.DateField(verbose_name='Disponível até')),
                ('documento_quantidade_partes', models.IntegerField(verbose_name='Quantas partes')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
            },
        ),
        migrations.CreateModel(
            name='Tipo_documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_tipo_documento', models.CharField(max_length=50, verbose_name='Tipo de documento')),
            ],
            options={
                'verbose_name': 'Tipo de documento',
                'verbose_name_plural': 'Tipos de documentos',
            },
        ),
        migrations.AddField(
            model_name='documento',
            name='tipo_documento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='services.Tipo_documento'),
        ),
    ]
