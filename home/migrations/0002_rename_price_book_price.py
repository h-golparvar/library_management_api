# Generated by Django 4.1.6 on 2023-08-17 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Price',
            new_name='price',
        ),
    ]