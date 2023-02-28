# Generated by Django 4.1.7 on 2023-02-28 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelentryexit', '0003_alter_hostel_h_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollnum_1', models.IntegerField()),
                ('rollnum_2', models.IntegerField()),
                ('name_1', models.CharField(max_length=100)),
                ('name_2', models.CharField(max_length=100)),
                ('in_time', models.BooleanField()),
                ('out_time', models.BooleanField()),
            ],
        ),
    ]
