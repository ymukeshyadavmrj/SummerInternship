# Generated by Django 3.0.3 on 2020-05-14 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20200514_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webpage',
            name='topic',
        ),
        migrations.DeleteModel(
            name='AccessRecord',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.DeleteModel(
            name='Webpage',
        ),
    ]
