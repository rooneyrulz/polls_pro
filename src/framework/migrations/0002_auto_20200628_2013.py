# Generated by Django 3.0.6 on 2020-06-28 14:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('framework', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='framework',
            name='vote',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]