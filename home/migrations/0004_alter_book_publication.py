# Generated by Django 4.1.6 on 2023-08-27 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]