# Generated by Django 2.2 on 2022-05-12 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_wow_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wow',
            name='caption',
            field=models.IntegerField(max_length=200),
        ),
    ]