# Generated by Django 3.2 on 2021-05-02 12:10

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractBaseCopyright',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(8), django.core.validators.MaxValueValidator(8)])),
                ('is_allowable', models.BooleanField(default=True)),
                ('accept_monetization', models.BooleanField(default=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), blank=True, null=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Restrictions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_private', models.BooleanField(default=False)),
                ('is_adult_content', models.BooleanField(default=False)),
                ('is_kids_content', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Restriction',
                'verbose_name_plural': 'Restrictions',
            },
        ),
        migrations.CreateModel(
            name='GameCopyright',
            fields=[
                ('abstractbasecopyright_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='additional.abstractbasecopyright')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
            ],
            bases=('additional.abstractbasecopyright',),
        ),
        migrations.CreateModel(
            name='SongCopyright',
            fields=[
                ('abstractbasecopyright_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='additional.abstractbasecopyright')),
                ('song', models.CharField(max_length=64)),
                ('artist', models.CharField(max_length=64)),
                ('album', models.CharField(max_length=64)),
                ('licensed_to', models.TextField()),
            ],
            bases=('additional.abstractbasecopyright',),
        ),
    ]
