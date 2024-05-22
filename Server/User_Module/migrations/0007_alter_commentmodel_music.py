# Generated by Django 5.0.2 on 2024-05-10 19:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Module', '0006_alter_commentmodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='music',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='User_Module.musicmodel', verbose_name='موزیک'),
        ),
    ]
