# Generated by Django 4.2.2 on 2023-06-24 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_cashbookentry_date_alter_cashbookentry_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashbookentry',
            name='date',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cashbookentry',
            name='month',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cashbookentry',
            name='year',
            field=models.IntegerField(),
        ),
    ]
