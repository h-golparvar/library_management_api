# Generated by Django 4.1.6 on 2023-08-19 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_otpcode_sender'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemebershiPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cost', models.PositiveIntegerField()),
                ('days', models.PositiveIntegerField()),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='otpcode',
            name='status',
            field=models.CharField(choices=[('succeccful', 'succeccful'), ('failed', 'failed'), ('pending', 'pending'), ('break', 'break')], default='pending', max_length=10),
        ),
    ]