# Generated by Django 5.1.3 on 2024-11-13 12:00

import utils.model_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True, validators=[utils.model_validators.validate_no_null_chars]),
        ),
    ]