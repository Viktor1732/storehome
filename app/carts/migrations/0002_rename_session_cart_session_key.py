# Generated by Django 4.2.16 on 2024-11-12 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='session',
            new_name='session_key',
        ),
    ]