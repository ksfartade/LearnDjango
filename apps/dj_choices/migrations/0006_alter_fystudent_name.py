# Generated by Django 5.0.6 on 2024-07-16 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_choices', '0005_alter_fystudent_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fystudent',
            name='name',
            field=models.CharField(blank=True, default='pankaj', max_length=100),
            preserve_default=False,
        ),
    ]
