# Generated by Django 5.1 on 2024-08-24 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0011_alter_country_alpha2code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='alpha2Code',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
