# Generated by Django 3.0 on 2020-03-30 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('status_string', models.CharField(default='Not Available', max_length=30)),
                ('tutor_location', models.CharField(default='Anywhere', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
