# Generated by Django 5.1.3 on 2025-01-19 13:20

import accounts.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', accounts.manager.UserManager()),
            ],
        ),
    ]
