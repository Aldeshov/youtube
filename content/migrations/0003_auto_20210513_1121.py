# Generated by Django 3.2 on 2021-05-13 05:21

import django.contrib.postgres.fields
from django.db import migrations, models
import tools.validators


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_alter_videocontent_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videocontent',
            name='playlist',
        ),
        migrations.AddField(
            model_name='playlist',
            name='contents',
            field=models.ManyToManyField(blank=True, null=True, to='content.VideoContent'),
        ),
        migrations.AlterField(
            model_name='status',
            name='short_videos',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FileField(upload_to='statuses', validators=[tools.validators.validate_size, tools.validators.validate_extension]), max_length=5, size=None),
        ),
    ]
