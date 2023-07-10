# Generated by Django 4.2 on 2023-06-08 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_members'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Members',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='coursecode',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='coursename',
            new_name='desc',
        ),
        migrations.RemoveField(
            model_name='course',
            name='coursedate',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
