# Generated by Django 3.2.9 on 2021-11-08 06:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kiroku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(default=django.utils.timezone.now)),
                ('moyori_cnt', models.IntegerField()),
                ('moe_cnt', models.IntegerField()),
            ],
        ),
    ]
