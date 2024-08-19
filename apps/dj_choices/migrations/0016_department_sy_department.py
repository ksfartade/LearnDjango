# Generated by Django 5.0.6 on 2024-07-16 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_choices', '0015_alter_sy_elective'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('ENTC', 'Electronics and telecommunications'), ('CIVIL', 'Cement and Intelligent'), ('CS', 'Computer science'), ('IT', 'Information Technology')], default='CIVIL', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='sy',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dj_choices.department'),
        ),
    ]
