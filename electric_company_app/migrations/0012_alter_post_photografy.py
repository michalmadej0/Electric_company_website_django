# Generated by Django 4.1.5 on 2023-01-06 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electric_company_app', '0011_alter_post_photografy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photografy',
            field=models.ImageField(blank=True, null=True, upload_to='media/posts/'),
        ),
    ]
