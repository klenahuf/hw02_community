# Generated by Django 2.2.19 on 2022-10-26 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20221026_0901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='text',
            new_name='title',
        ),
    ]
