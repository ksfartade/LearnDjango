# Generated by Django 5.0.6 on 2024-07-16 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_choices', '0006_alter_fystudent_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fystudent',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
