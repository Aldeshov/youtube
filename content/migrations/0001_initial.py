# Generated by Django 3.2 on 2021-05-12 18:42

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import tools.random_generate


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('applications', '0001_initial'),
        ('additional', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.IntegerField(default=tools.random_generate.random_key, unique=True)),
                ('title', models.CharField(max_length=64)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to='applications.channel')),
            ],
        ),
        migrations.CreateModel(
            name='VideoContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=tools.random_generate.random_code, max_length=16, unique=True)),
                ('title', models.CharField(max_length=64)),
                ('video', models.FileField(upload_to='contents')),
                ('type', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Musics'), (2, 'Sports'), (3, 'Gaming'), (4, 'News'), (5, 'Live'), (6, '360 Video')])),
                ('description', models.TextField()),
                ('_disliked', models.ManyToManyField(blank=True, related_name='content_videocontent_dislikes', to='applications.Channel')),
                ('_liked', models.ManyToManyField(blank=True, related_name='content_videocontent_likes', to='applications.Channel')),
                ('_viewed', models.ManyToManyField(blank=True, related_name='content_videocontent_views', to='applications.Channel')),
                ('copyrights', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='additional.copyrights')),
                ('on_channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='applications.channel')),
                ('playlist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='contents', to='content.playlist')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=tools.random_generate.random_code, max_length=16, unique=True)),
                ('title', models.CharField(max_length=64)),
                ('short_videos', django.contrib.postgres.fields.ArrayField(base_field=models.FileField(upload_to='statuses'), max_length=5, size=None)),
                ('_disliked', models.ManyToManyField(blank=True, related_name='content_status_dislikes', to='applications.Channel')),
                ('_liked', models.ManyToManyField(blank=True, related_name='content_status_likes', to='applications.Channel')),
                ('_viewed', models.ManyToManyField(blank=True, related_name='content_status_views', to='applications.Channel')),
                ('on_channel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='applications.channel')),
            ],
            options={
                'verbose_name_plural': 'Statuses',
            },
        ),
        migrations.CreateModel(
            name='CommunityContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=tools.random_generate.random_code, max_length=16, unique=True)),
                ('title', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('_disliked', models.ManyToManyField(blank=True, related_name='content_communitycontent_dislikes', to='applications.Channel')),
                ('_liked', models.ManyToManyField(blank=True, related_name='content_communitycontent_likes', to='applications.Channel')),
                ('_viewed', models.ManyToManyField(blank=True, related_name='content_communitycontent_views', to='applications.Channel')),
                ('on_channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_contents', to='applications.channel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='content.videocontent')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='applications.channel')),
            ],
        ),
    ]
