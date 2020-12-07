# Generated by Django 2.2 on 2020-12-07 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=20)),
                ('customer_displya_name', models.CharField(max_length=20)),
                ('customer_email', models.EmailField(max_length=254)),
                ('customer_phone', models.IntegerField()),
                ('website', models.CharField(max_length=20)),
            ],
        ),
    ]
