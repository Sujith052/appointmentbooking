# Generated by Django 5.1.4 on 2024-12-17 06:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appointment_time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_time', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='time_slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeslote', models.CharField(max_length=50)),
                ('appointment_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='users.appointment_time')),
            ],
        ),
    ]
