# Generated by Django 4.0.5 on 2022-06-08 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-time_create'], 'verbose_name': 'Посты', 'verbose_name_plural': 'Посты'},
        ),
    ]
