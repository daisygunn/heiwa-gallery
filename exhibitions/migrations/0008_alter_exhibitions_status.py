# Generated by Django 3.2 on 2022-04-12 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitions', '0007_auto_20220410_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibitions',
            name='status',
            field=models.CharField(choices=[('finished', 'finished'), ('now_showing', 'now_showing'), ('coming_soon', 'coming_soon'), ('pending', 'pending'), ('cancelled', 'cancelled')], default='now showing', max_length=254),
        ),
    ]