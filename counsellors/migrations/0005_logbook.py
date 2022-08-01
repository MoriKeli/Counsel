# Generated by Django 4.0.3 on 2022-07-29 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counsellors', '0004_alter_workprofile_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogBook',
            fields=[
                ('id', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('patient', models.TextField(max_length=150)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('counsellor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counsellors.counsellorprofile')),
            ],
            options={
                'verbose_name_plural': 'Log Book',
                'ordering': ['created'],
            },
        ),
    ]