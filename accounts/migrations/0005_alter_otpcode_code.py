# Generated by Django 4.1.6 on 2023-08-17 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_otpcode_remove_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpcode',
            name='code',
            field=models.IntegerField(blank=True),
        ),
    ]
