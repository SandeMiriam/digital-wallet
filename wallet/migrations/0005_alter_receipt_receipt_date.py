# Generated by Django 4.0.6 on 2022-08-25 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_rename_isactive_wallet_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='receipt_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
