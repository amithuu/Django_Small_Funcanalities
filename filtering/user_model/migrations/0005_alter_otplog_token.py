# Generated by Django 3.2.23 on 2024-02-07 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_model', '0004_otplog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otplog',
            name='token',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
