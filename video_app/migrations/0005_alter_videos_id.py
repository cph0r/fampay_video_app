# Generated by Django 3.2.5 on 2021-07-08 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_app', '0004_api_keys_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]