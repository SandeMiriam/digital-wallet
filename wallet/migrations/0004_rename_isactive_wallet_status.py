# Generated by Django 4.0.6 on 2022-08-02 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_card_signature_customer_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wallet',
            old_name='isactive',
            new_name='status',
        ),
    ]
