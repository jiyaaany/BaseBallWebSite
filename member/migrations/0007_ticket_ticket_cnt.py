# Generated by Django 3.0.5 on 2020-07-14 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_ticket_is_del'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ticket_cnt',
            field=models.IntegerField(default=0),
        ),
    ]
