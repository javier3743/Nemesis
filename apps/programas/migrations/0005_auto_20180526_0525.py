# Generated by Django 2.0.4 on 2018-05-26 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programas', '0004_auto_20180419_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=15)),
                ('Facultad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programas.Facultad')),
            ],
        ),
        migrations.RemoveField(
            model_name='programaacademico',
            name='Facultad',
        ),
    ]