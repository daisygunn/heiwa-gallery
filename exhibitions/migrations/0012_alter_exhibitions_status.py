# Generated by Django 3.2 on 2022-04-12 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitions', '0011_alter_exhibitions_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibitions',
            name='status',
            field=models.CharField(choices=[('finished', 'finished'), ('now showing', 'now showing'), ('coming soon', 'coming soon'), ('pending', 'pending'), ('cancelled', 'cancelled')], default='now showing', max_length=254),
        ),
    ]
