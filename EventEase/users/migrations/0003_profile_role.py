# Generated by Django 5.1.3 on 2024-11-20 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_bio_remove_profile_user_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('User', 'User')], default='User', max_length=10),
        ),
    ]
