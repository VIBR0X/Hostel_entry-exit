# Generated by Django 4.1.7 on 2023-02-24 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelentryexit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='h_num',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]