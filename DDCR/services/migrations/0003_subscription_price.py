# Generated by Django 4.2.4 on 2023-09-05 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_rename_plan_tupe_plan_plan_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
