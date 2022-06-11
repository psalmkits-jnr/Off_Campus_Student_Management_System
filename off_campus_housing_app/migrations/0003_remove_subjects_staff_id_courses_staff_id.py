# Generated by Django 4.0.4 on 2022-05-22 00:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('off_campus_housing_app', '0002_alter_customuser_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='staff_id',
        ),
        migrations.AddField(
            model_name='courses',
            name='staff_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
