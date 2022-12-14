# Generated by Django 4.0.3 on 2022-07-28 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_userappointment_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.CharField(editable=False, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('msg', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
            options={
                'verbose_name_plural': 'Testimonials',
                'ordering': ['created'],
            },
        ),
    ]
