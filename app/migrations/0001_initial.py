# Generated by Django 4.1.5 on 2023-02-11 16:03

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
            name='Elmagmo3a',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='الاسم')),
                ('type_magmo3a', models.CharField(blank=True, max_length=32, null=True)),
                ('descrebtion', models.TextField(blank=True, default='', max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'المجموعة',
                'verbose_name_plural': 'المجموعات',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='الاسم')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=12, verbose_name='رقم التليفون')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'البروفايل',
                'verbose_name_plural': 'بروفايلات المستخدمين',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='اسم المنتج')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='السعر')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_create', models.DateField(blank=True, null=True)),
                ('model_prod', models.CharField(blank=True, max_length=30, null=True, verbose_name='الموديل')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product', verbose_name='صورة المنتج')),
                ('category', models.CharField(blank=True, max_length=50, null=True, verbose_name='المجموعة')),
                ('actav', models.BooleanField(blank=True, null=True, verbose_name='الحالة')),
                ('active', models.BooleanField(default=True, verbose_name='نشيط ؟')),
                ('count', models.IntegerField(verbose_name='الكمية')),
                ('type_product', models.CharField(blank=True, choices=[('1', 'جهاز'), ('2', 'اكسسوار'), ('3', 'غير ذلك')], max_length=320, null=True)),
                ('slug', models.SlugField()),
                ('magmo3a', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.elmagmo3a', verbose_name='المجموعة')),
                ('tag', models.ManyToManyField(blank=True, to='app.tag', verbose_name='Tag')),
            ],
            options={
                'verbose_name': 'المنتج',
                'verbose_name_plural': 'المنتجات',
            },
        ),
    ]
