# Generated by Django 5.0.2 on 2024-05-09 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Module', '0003_musicmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicmodel',
            name='title',
            field=models.CharField(default='', max_length=300, verbose_name='عنوان'),
            preserve_default=False,
        ),
    ]
