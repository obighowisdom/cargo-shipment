# Generated by Django 2.2 on 2022-05-12 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_delete_tools'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wow',
            name='caption',
            field=models.CharField(max_length=200),
        ),
    ]
