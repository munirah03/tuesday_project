# Generated by Django 4.2 on 2023-04-17 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course_code',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registration.course'),
            preserve_default=False,
        ),
    ]
