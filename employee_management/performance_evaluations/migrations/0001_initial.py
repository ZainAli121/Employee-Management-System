# Generated by Django 5.0.1 on 2024-01-19 12:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerformanceEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rating', models.IntegerField()),
                ('comments', models.TextField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_info.employee')),
            ],
        ),
    ]
