# Generated by Django 4.2 on 2023-05-18 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClientId', models.CharField(max_length=100)),
                ('ClientName', models.TextField(max_length=100)),
                ('ClientPhone', models.CharField(max_length=100)),
                ('Gender', models.TextField(max_length=100)),
            ],
        ),
    ]
