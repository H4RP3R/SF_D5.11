# Generated by Django 3.0.7 on 2020-06-09 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0005_auto_20200609_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
    ]
