# Generated by Django 4.1.7 on 2023-02-28 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelentryexit', '0005_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='rollnum_1',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='database',
            name='rollnum_2',
            field=models.CharField(max_length=20),
        ),
    ]
