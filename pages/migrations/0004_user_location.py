# Generated by Django 4.1.4 on 2022-12-12 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_reason_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
