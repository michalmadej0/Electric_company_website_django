# Generated by Django 4.1.5 on 2023-01-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electric_company_app', '0015_remove_post_photografy_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
    ]
