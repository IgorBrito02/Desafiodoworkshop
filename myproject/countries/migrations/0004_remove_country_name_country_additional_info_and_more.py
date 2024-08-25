# Generated by Django 5.1 on 2024-08-24 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0003_country_common_name_alter_country_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='name',
        ),
        migrations.AddField(
            model_name='country',
            name='additional_info',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='common_name',
            field=models.CharField(max_length=100),
        ),
    ]
