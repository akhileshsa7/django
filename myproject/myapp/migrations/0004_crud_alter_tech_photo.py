# Generated by Django 5.0.6 on 2024-06-04 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_tech_alter_emplo_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='crud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=15)),
                ('LAST_NAME', models.CharField(max_length=5)),
                ('AGE', models.IntegerField(max_length=2)),
                ('GMAIL', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'CRUD OPERATIONS',
            },
        ),
        migrations.AlterField(
            model_name='tech',
            name='photo',
            field=models.ImageField(upload_to='uploded_images/'),
        ),
    ]
