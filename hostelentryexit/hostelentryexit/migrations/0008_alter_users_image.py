# Generated by Django 4.1.7 on 2023-03-02 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelentryexit', '0007_rename_student_image_users_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]