# Generated by Django 4.0 on 2022-01-07 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0005_alter_persona_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='hoja_vida',
        ),
        migrations.AddField(
            model_name='persona',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado', verbose_name='Foto'),
        ),
    ]