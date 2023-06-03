# Generated by Django 4.0.10 on 2023-02-25 20:46

import core.user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(db_index=True, default=core.user.models.generate_user_uuid, editable=False, max_length=15, verbose_name='User ID'),
        ),
    ]
