# Generated by Django 2.2.13 on 2020-06-09 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='title',
            field=models.CharField(default='', max_length=70),
        ),
    ]
