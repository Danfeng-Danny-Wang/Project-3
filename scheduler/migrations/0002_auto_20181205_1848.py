# Generated by Django 2.1.3 on 2018-12-06 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_1', models.TextField(max_length=200)),
                ('activity_2', models.TextField(max_length=200)),
                ('activity_3', models.TextField(max_length=200)),
                ('activity_4', models.TextField(max_length=200)),
                ('activity_5', models.TextField(max_length=200)),
                ('activity_6', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Schedule')),
            ],
        ),
        migrations.AddField(
            model_name='day',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Week'),
        ),
    ]
