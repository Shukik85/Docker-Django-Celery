# Generated by Django 4.2.4 on 2023-09-05 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_subscription_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='full_price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]