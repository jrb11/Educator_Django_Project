# Generated by Django 4.0.3 on 2022-06-09 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu_home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educator',
            name='edu_exp',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='educator',
            name='edu_major',
            field=models.CharField(max_length=10),
        ),
    ]
