# Generated by Django 4.2.4 on 2023-11-30 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_category', models.CharField(max_length=200)),
                ('c_description', models.TextField()),
                ('c_image', models.ImageField(blank=True, null=True, upload_to='courses/category')),
            ],
        ),
    ]
