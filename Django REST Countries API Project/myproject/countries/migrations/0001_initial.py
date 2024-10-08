# Generated by Django 5.1 on 2024-08-16 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('capital', models.CharField(max_length=400)),
                ('population', models.IntegerField()),
                ('region', models.CharField(max_length=400)),
                ('subregion', models.CharField(max_length=400)),
                ('alpha2Code', models.CharField(max_length=10)),
                ('alpha3Code', models.CharField(max_length=10)),
            ],
        ),
    ]
