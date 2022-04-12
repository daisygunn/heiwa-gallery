# Generated by Django 3.2 on 2022-04-10 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitions', '0006_alter_exhibitions_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibitions',
            name='description',
            field=models.TextField(blank=True, max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='exhibitions',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='exhibitions',
            name='photographer_artist',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='exhibitions',
            name='style',
            field=models.CharField(choices=[('photography', 'photography'), ('sculpture', 'sculpture'), ('painting', 'painting'), ('video', 'video')], default=1, max_length=15),
        ),
    ]