# Generated by Django 5.0.6 on 2024-08-06 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_choices', '0021_alter_department_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
