# Generated by Django 4.2.2 on 2023-06-24 10:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0005_rename_user_member_active_user_member_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cashbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('financial_year', models.CharField(max_length=7, validators=[django.core.validators.RegexValidator(message="Financial year must be in the format 'YYYY-YY'", regex='^\\d{4}-\\d{2}$')])),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cashbooks', to='member.member')),
            ],
        ),
        migrations.CreateModel(
            name='CashBookEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=2)),
                ('month', models.CharField(max_length=2)),
                ('year', models.CharField(max_length=4)),
                ('fund_type', models.CharField(choices=[('INTEREST', 'Interest'), ('ADJUSTMENT', 'Adjustment'), ('CHEQUE', 'Cheque'), ('SERVICE_FEE', 'Service Fee'), ('OTHER', 'Other')], max_length=20)),
                ('refund_on_exit_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('deposits_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('loan_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cashbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='accounts.cashbook')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
            ],
        ),
    ]