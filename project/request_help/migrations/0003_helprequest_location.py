# Generated by Django 3.0.3 on 2020-02-27 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_help', '0002_remove_helprequest_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='helprequest',
            name='location',
            field=models.CharField(default='Rice Hall', max_length=100),
        ),
    ]
