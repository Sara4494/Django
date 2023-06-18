# Generated by Django 4.1.6 on 2023-04-05 01:24

import datetime
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
            name='ACategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Trendy_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo7', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('details', models.TextField(blank=True, max_length=1000, null=True)),
                ('colors', models.CharField(blank=True, max_length=20, null=True)),
                ('size', models.CharField(blank=True, choices=[('s', 's'), ('m', 'm'), ('l', 'l'), ('xl', 'xl')], max_length=10, null=True)),
                ('publish_dete', models.DateTimeField(default=datetime.datetime.now)),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='Slug')),
                ('categor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='app.acategory')),
            ],
            options={
                'ordering': ['publish_dete'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='الاسم الاول')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='اللقب')),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True, verbose_name='رقم التليفون')),
                ('phone_number2', models.CharField(blank=True, max_length=11, null=True, verbose_name='رقم التليفون 2')),
                ('addres', models.CharField(blank=True, max_length=300, null=True, verbose_name='العنوان')),
                ('area', models.CharField(blank=True, max_length=50, null=True, verbose_name='المنقطة')),
                ('mailo', models.EmailField(blank=True, max_length=254, null=True, verbose_name='ايميل (بالشركة)')),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='صورة شخصية')),
                ('pos_in_store', models.CharField(blank=True, choices=[('admin', 'Admin'), ('Customer', 'Customer'), ('Tager', 'Tager')], max_length=50, null=True, verbose_name='صفته بالموقع')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='Slug')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]