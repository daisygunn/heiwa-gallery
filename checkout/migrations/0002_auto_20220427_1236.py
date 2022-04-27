# Generated by Django 3.2 on 2022-04-27 12:36

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(
                default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(default='blank', max_length=20),
            preserve_default=False,
        ),
    ]