# Generated by Django 5.1.4 on 2024-12-17 09:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_appointbooking_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointmentbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.BigIntegerField()),
                ('date', models.DateField()),
                ('booking_status', models.CharField(max_length=50)),
                ('selected_slote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_slot', to='users.time_slot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='users.userdata')),
            ],
        ),
        migrations.DeleteModel(
            name='appointbooking',
        ),
    ]
