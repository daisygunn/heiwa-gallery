# Generated by Django 3.2 on 2022-04-07 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitions', '0004_alter_exhibitions_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exhibitions',
            old_name='now_showing',
            new_name='display',
        ),
    ]