# Generated by Django 3.1 on 2020-12-19 21:08

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_firstName', models.CharField(blank=True, max_length=30, verbose_name='İsim')),
                ('contact_lastName', models.CharField(blank=True, max_length=30, verbose_name='Soyisim')),
                ('contact_email', models.EmailField(max_length=30, verbose_name='E-mail')),
                ('contact_subject', models.CharField(max_length=20, verbose_name='Konu')),
                ('contact_message', ckeditor_uploader.fields.RichTextUploadingField(max_length=2000, verbose_name='Mesaj')),
                ('contact_status', models.CharField(choices=[('New', 'New'), ('Read', 'Read')], default='new', max_length=10)),
                ('contact_ip', models.CharField(blank=True, max_length=20)),
                ('contact_note', models.CharField(blank=True, max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=40, verbose_name='Başlık')),
                ('keywords', models.CharField(blank=True, max_length=255, verbose_name='Anahtar Kelimeler')),
                ('description', models.CharField(blank=True, max_length=40, verbose_name='Açıklama')),
                ('company', models.CharField(blank=True, max_length=40, verbose_name='Şirket Adı')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='Adres')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Telefon')),
                ('fax', models.CharField(blank=True, max_length=20, verbose_name='Faks')),
                ('email', models.CharField(blank=True, max_length=30, verbose_name='E-Mail')),
                ('smtpServer', models.CharField(blank=True, max_length=20, verbose_name='SMTP Server')),
                ('smtpEmail', models.CharField(blank=True, max_length=30, verbose_name='SMTP Email')),
                ('smtpPassword', models.CharField(blank=True, max_length=20, verbose_name='SMTP Pass')),
                ('smtpPort', models.CharField(blank=True, max_length=5)),
                ('icon', models.ImageField(blank=True, upload_to='images/')),
                ('facebook', models.CharField(blank=True, max_length=40, verbose_name='Facebook')),
                ('instagram', models.CharField(blank=True, max_length=40, verbose_name='İnstagram')),
                ('twitter', models.CharField(blank=True, max_length=40, verbose_name='Twitter')),
                ('aboutUs', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Hakkımızda')),
                ('contact', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='İletişim')),
                ('references', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Referanslar')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(blank=True, max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]