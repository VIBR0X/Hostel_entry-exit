# Generated by Django 4.1.7 on 2023-03-02 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostelentryexit', '0006_rename_image_users_student_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='student_image',
            new_name='image',
        ),
    ]
