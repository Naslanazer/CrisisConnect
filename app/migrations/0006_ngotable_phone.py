# Generated by Django 5.1.4 on 2024-12-15 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_donation_donationtable_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngotable',
            name='Phone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
