# Generated by Django 4.2.3 on 2023-08-05 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_action_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='res',
            field=models.CharField(max_length=200, null=True),
        ),
    ]