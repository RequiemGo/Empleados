# Generated by Django 4.0 on 2021-12-16 19:47

import ckeditor.fields
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_habilidades_alter_persona_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
