# Generated by Django 2.2.6 on 2020-08-24 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0003_auto_20200821_1655'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hostmodel',
            options={'verbose_name': 'meeting', 'verbose_name_plural': 'meeting'},
        ),
        migrations.AlterModelTable(
            name='hostmodel',
            table=None,
        ),
    ]
