# Generated by Django 3.0.5 on 2023-11-20 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=2)),
                ('date', models.CharField(max_length=10)),
                ('task', models.CharField(max_length=200)),
            ],
        ),
    ]
