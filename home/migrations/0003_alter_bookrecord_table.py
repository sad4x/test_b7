# Generated by Django 4.2.4 on 2023-08-25 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_student_age_alter_student_gender_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='bookrecord',
            table='Book',
        ),
    ]
