# Generated by Django 4.2.4 on 2023-12-01 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='c_image',
            new_name='image',
        ),
    ]
