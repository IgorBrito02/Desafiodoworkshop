# Generated by Django 5.1 on 2024-08-24 04:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0004_remove_country_name_country_additional_info_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='common_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='country',
            name='additional_info',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='country',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countries.region'),
        ),
        migrations.AlterField(
            model_name='country',
            name='subregion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countries.subregion'),
        ),
    ]
