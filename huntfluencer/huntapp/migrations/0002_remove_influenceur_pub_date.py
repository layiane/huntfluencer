# Generated by Django 4.1.3 on 2022-11-16 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("huntapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="influenceur", name="pub_date",),
    ]
