# Generated by Django 4.0.4 on 2022-05-22 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('off_campus_housing_app', '0007_alter_subjects_course_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='course_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='off_campus_housing_app.courses'),
        ),
    ]
