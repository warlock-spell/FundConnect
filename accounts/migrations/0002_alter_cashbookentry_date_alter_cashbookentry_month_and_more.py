# Generated by Django 4.2.2 on 2023-06-24 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashbookentry',
            name='date',
            field=models.IntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name='cashbookentry',
            name='month',
            field=models.IntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name='cashbookentry',
            name='year',
            field=models.IntegerField(max_length=4),
        ),
    ]