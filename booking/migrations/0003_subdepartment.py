# Generated by Django 5.2.1 on 2025-05-23 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_booking_modified_by_alter_booking_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subdepartment',
            fields=[
                ('subdepartment_id', models.AutoField(primary_key=True, serialize=False)),
                ('subdepartment_name', models.CharField(max_length=100)),
            ],
        ),
    ]
