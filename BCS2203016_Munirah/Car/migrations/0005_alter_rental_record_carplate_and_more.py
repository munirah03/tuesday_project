# Generated by Django 4.2 on 2023-05-18 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0004_rental_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental_record',
            name='CarPlate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Car.car'),
        ),
        migrations.AlterField(
            model_name='rental_record',
            name='ClientId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Car.client'),
        ),
    ]
