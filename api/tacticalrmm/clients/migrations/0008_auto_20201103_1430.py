# Generated by Django 3.1.2 on 2020-11-03 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_auto_20201102_1920'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='site',
            options={'ordering': ('name',)},
        ),
    ]