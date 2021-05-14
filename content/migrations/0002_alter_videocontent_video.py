# Generated by Django 3.2 on 2021-05-13 05:07

from django.db import migrations, models
import tools.validators


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videocontent',
            name='video',
            field=models.FileField(upload_to='contents', validators=[tools.validators.validate_size, tools.validators.validate_extension]),
        ),
    ]
