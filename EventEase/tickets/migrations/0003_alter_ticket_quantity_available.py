# Generated by Django 5.1.3 on 2024-11-16 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_ticket_created_at_ticket_quantity_ticket_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='quantity_available',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]