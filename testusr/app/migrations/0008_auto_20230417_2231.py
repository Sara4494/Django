# Generated by Django 3.2.18 on 2023-04-17 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_profile_first_name_remove_profile_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photo/', verbose_name='Profile photos'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=11, null=True, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number2',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Phone number'),
        ),
    ]
