# Generated by Django 4.2.4 on 2023-08-25 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_alter_photopost_image2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photopost',
            name='image1',
            field=models.ImageField(upload_to='photos', verbose_name='イメージ1'),
        ),
        migrations.AlterField(
            model_name='photopost',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='イメージ2'),
        ),
    ]
