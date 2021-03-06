# Generated by Django 4.0.2 on 2022-02-22 05:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='remainderData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('quota', models.CharField(max_length=1000)),
                ('user_id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
            ],
        ),
    ]
