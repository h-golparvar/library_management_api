# Generated by Django 4.1.6 on 2023-08-27 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_book_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='shabak',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
