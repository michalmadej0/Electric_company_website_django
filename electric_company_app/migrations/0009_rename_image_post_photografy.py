# Generated by Django 4.1.5 on 2023-01-06 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electric_company_app', '0008_alter_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='photografy',
        ),
    ]
