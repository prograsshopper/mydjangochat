# Generated by Django 5.0.7 on 2024-11-17 08:38

import mysite.json_extended
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_roommember_room_online_user_set'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roommember',
            name='channel_names',
            field=models.JSONField(decoder=mysite.json_extended.ExtendedJSONDecoder, default=set, encoder=mysite.json_extended.ExtendedJSONEncoder),
        ),
    ]