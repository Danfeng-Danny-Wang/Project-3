# Generated by Django 2.1.3 on 2018-12-06 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_auto_20181205_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='week_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
