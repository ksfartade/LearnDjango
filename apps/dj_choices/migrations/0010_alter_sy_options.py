# Generated by Django 5.0.6 on 2024-07-16 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dj_choices', '0009_alter_sy_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sy',
            options={'default_permissions': 'view', 'ordering': ['division', '-name'], 'verbose_name': 'SY Student Data', 'verbose_name_plural': 'SY Student Records'},
        ),
    ]
