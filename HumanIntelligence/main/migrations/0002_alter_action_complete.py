# Generated by Django 4.2.3 on 2023-08-04 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]