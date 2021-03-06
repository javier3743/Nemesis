# Generated by Django 2.0.4 on 2018-04-18 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_dean',
            field=models.BooleanField(default=False, verbose_name='dean status'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_director',
            field=models.BooleanField(default=False, verbose_name='director status'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(default=False, verbose_name='teacher status'),
        ),
    ]
