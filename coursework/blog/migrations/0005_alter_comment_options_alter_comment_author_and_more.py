# Generated by Django 4.0.5 on 2023-05-30 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-time_create'], 'verbose_name': 'Коментар', 'verbose_name_plural': 'Коментарі'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(blank=True, verbose_name='Текст комментарію'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Пост'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='related_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.comment', verbose_name='Связанный комментарий'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Час створення'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Час оновлення'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
