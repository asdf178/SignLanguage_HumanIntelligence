# Generated by Django 4.2.3 on 2023-08-05 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_action_res'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='action',
            name='res',
        ),
    ]
