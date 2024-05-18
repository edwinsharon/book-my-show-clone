# Generated by Django 5.0.6 on 2024-05-17 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bmsuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='moviedetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moviename', models.CharField(max_length=200)),
                ('rating', models.CharField(max_length=150)),
                ('appearence', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=150)),
                ('certification', models.CharField(max_length=50)),
                ('releasedate', models.CharField(max_length=50)),
                ('poster', models.ImageField(upload_to='')),
                ('banner', models.ImageField(upload_to='')),
            ],
        ),
    ]