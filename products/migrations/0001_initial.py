# Generated by Django 3.1 on 2020-12-19 21:08

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Başlık')),
                ('keywords', models.CharField(max_length=255, verbose_name='Anahtar Kelimeler')),
                ('description', models.CharField(max_length=255, verbose_name='Kategori Açıklaması')),
                ('image', models.ImageField(blank=True, upload_to='images/', verbose_name='Kategori Fotoğrafı')),
                ('status', models.CharField(choices=[('True', 'Aktif'), ('False', 'Aktif Değil')], max_length=10, verbose_name='Kategori Durumu')),
                ('slug', models.SlugField(unique=True, verbose_name='Kategori Etiketi')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=40, verbose_name='Başlık')),
                ('keywords', models.CharField(blank=True, max_length=255, verbose_name='Anahtar Kelimeler')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Ürün Açıklaması')),
                ('image', models.ImageField(blank=True, upload_to='images/', verbose_name='Ürün Fotoğrafı')),
                ('image2', models.ImageField(blank=True, upload_to='images/', verbose_name='Ürün Fotoğrafı 2')),
                ('image3', models.ImageField(blank=True, upload_to='images/', verbose_name='Ürün Fotoğrafı 3')),
                ('price', models.FloatField(blank=True, verbose_name='Fiyat')),
                ('amount', models.IntegerField(blank=True, verbose_name='Adet')),
                ('slug', models.SlugField(unique=True)),
                ('detail', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Ürün Detayı')),
                ('status', models.CharField(blank=True, choices=[('True', 'Stokta Var'), ('False', 'Stokta Yok')], max_length=10, verbose_name='Ürün Durumu')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='Başlık')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='images/', verbose_name='Fotoğraf')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]