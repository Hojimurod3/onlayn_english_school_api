# Generated by Django 5.0.2 on 2024-03-15 13:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='kurs.branch'),
        ),
    ]
