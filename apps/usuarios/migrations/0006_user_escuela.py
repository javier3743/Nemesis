# Generated by Django 2.0.4 on 2018-06-22 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programas', '0005_auto_20180526_0525'),
        ('usuarios', '0005_auto_20180419_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='escuela',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='programas.Escuela'),
        ),
    ]
