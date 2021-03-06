# Generated by Django 2.0.4 on 2018-04-18 23:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='Profesor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='curso',
            name='Habilitable',
            field=models.CharField(choices=[('S', 'Si'), ('No', 'No')], default='SI', max_length=2),
        ),
        migrations.AlterField(
            model_name='curso',
            name='Validable',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], default='SI', max_length=2),
        ),
    ]
