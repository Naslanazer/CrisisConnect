# Generated by Django 5.1.4 on 2025-01-20 06:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_tasktable_userid_assigntable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationtable',
            name='USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.usertable'),
        ),
    ]
