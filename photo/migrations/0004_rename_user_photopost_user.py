# Generated by Django 4.2.4 on 2023-08-25 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_alter_photopost_image1_alter_photopost_image2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photopost',
            old_name='User',
            new_name='user',
        ),
    ]
