# Generated by Django 4.0.3 on 2022-07-29 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counsellors', '0005_logbook'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logbook',
            old_name='counsellor',
            new_name='log_name',
        ),
    ]