# Generated by Django 4.0.6 on 2022-08-02 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=20)),
                ('account_type', models.CharField(max_length=15)),
                ('savings', models.IntegerField()),
                ('destination', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=40)),
                ('symbol', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Thirdparty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('transaction_cost', models.IntegerField()),
                ('isactive', models.BooleanField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Thirdparty_account', to='wallet.account')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Thirdparty_currency', to='wallet.account')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('isactive', models.CharField(max_length=15)),
                ('balance', models.IntegerField()),
                ('pin', models.TextField(max_length=15)),
                ('date', models.DateTimeField()),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.currency')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('amount', models.PositiveIntegerField()),
                ('transaction_type', models.CharField(max_length=10)),
                ('transaction_code', models.CharField(max_length=4)),
                ('charge', models.IntegerField()),
                ('status', models.CharField(max_length=10)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.customer')),
                ('thirdparty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.thirdparty')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_reward', models.DateTimeField()),
                ('points', models.IntegerField()),
                ('Wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reward_wallet', to='wallet.wallet')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reward_transaction', to='wallet.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_date', models.DateTimeField()),
                ('receipt_file', models.FileField(upload_to='')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Receipt_transaction', to='wallet.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField()),
                ('isactive', models.BooleanField()),
                ('message', models.CharField(max_length=100)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Notification_recipient', to='wallet.account')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_type', models.CharField(max_length=10)),
                ('amount', models.IntegerField()),
                ('date_and_time', models.DateTimeField()),
                ('loan_terms', models.CharField(max_length=10)),
                ('payment_due_date', models.DateTimeField()),
                ('guarantor', models.CharField(max_length=15)),
                ('balance', models.IntegerField()),
                ('duration', models.CharField(max_length=10)),
                ('interest_rates', models.IntegerField()),
                ('status', models.CharField(max_length=10)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Loan_wallet', to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=16)),
                ('card_name', models.CharField(max_length=20)),
                ('pin_number', models.CharField(max_length=4)),
                ('serial_code', models.PositiveSmallIntegerField()),
                ('expiry_date', models.DateTimeField()),
                ('card_status', models.CharField(max_length=10)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.account')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='wallet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet'),
        ),
    ]