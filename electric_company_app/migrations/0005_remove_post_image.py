# Generated by Django 4.1.5 on 2023-01-06 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electric_company_app', '0004_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]