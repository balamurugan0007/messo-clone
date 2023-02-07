# Generated by Django 4.1.5 on 2023-02-01 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='catogory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='static/upload')),
                ('description', models.TextField(max_length=300)),
                ('date', models.DateField()),
                ('status', models.BooleanField(default=False, help_text='0-show,1-Hidden')),
            ],
        ),
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('pass1', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('old_price', models.IntegerField()),
                ('new_price', models.IntegerField()),
                ('ratings', models.FloatField()),
                ('stocks', models.IntegerField()),
                ('image', models.ImageField(upload_to='static/upload')),
                ('description', models.TextField(max_length=300)),
                ('date', models.DateField()),
                ('status', models.BooleanField(default=False, help_text='0-show,1-Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0-default,1-Trending')),
            ],
        ),
    ]
