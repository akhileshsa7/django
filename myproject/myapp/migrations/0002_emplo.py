# Generated by Django 5.0.6 on 2024-06-03 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emplo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=15, verbose_name='FIRST NAME')),
                ('Last_Name', models.CharField(max_length=5, verbose_name='LAST NAME')),
                ('Gmail', models.CharField(max_length=20, verbose_name='GMAIL')),
                ('mobile', models.IntegerField(max_length=12, verbose_name='mobile number')),
                ('password', models.CharField(max_length=8, verbose_name='password')),
            ],
        ),
    ]