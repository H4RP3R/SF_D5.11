# Generated by Django 3.0.7 on 2020-06-16 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0017_auto_20200611_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='friend_reader',
            field=models.ManyToManyField(to='p_library.Friend'),
        ),
    ]
