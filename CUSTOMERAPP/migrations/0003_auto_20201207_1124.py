# Generated by Django 2.2 on 2020-12-07 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CUSTOMERAPP', '0002_auto_20201207_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcustomer',
            name='customer_email',
            field=models.EmailField(max_length=254),
        ),
    ]
