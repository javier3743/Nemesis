# Generated by Django 2.0.4 on 2018-04-18 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programas', '0002_auto_20180418_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='programaacademico',
            name='Escuela',
            field=models.CharField(max_length=50, null=True),
        ),
    ]