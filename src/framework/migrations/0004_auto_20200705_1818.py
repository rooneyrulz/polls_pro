# Generated by Django 3.0.6 on 2020-07-05 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0003_auto_20200629_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='framework',
            name='vote',
        ),
        migrations.AddField(
            model_name='framework',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]
