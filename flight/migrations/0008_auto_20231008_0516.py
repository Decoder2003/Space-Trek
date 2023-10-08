# Generated by Django 3.1.2 on 2023-10-07 23:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0007_remove_ticket_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='user',
        ),
        migrations.AddField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL),
        ),
    ]