# Generated by Django 4.0.4 on 2022-05-22 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('off_campus_housing_app', '0005_alter_courses_staff_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='staff_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='off_campus_housing_app.staffs'),
            preserve_default=False,
        ),
    ]
