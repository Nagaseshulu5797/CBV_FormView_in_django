# Generated by Django 4.1.7 on 2023-05-16 12:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_school_sid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='sid',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(999)]),
        ),
    ]
