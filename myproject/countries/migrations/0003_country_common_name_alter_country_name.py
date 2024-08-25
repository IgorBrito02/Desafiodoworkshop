# Generated by Django 5.1 on 2024-08-24 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_region_alter_country_alpha2code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='common_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
