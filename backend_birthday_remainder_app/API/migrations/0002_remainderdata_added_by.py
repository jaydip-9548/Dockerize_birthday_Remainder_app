# Generated by Django 4.0.2 on 2022-02-09 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API_SignIn_Up', '0001_initial'),
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='remainderdata',
            name='added_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='API_SignIn_Up.userdata'),
        ),
    ]
