# Generated by Django 4.0.2 on 2022-02-11 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0007_alter_remainderdata_photoname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remainderdata',
            name='photoName',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
