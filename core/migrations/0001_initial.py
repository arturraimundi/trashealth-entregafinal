# Generated by Django 5.1.1 on 2024-11-07 11:42

import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PontodeColeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to='local_de_coleta', variations={'thumb': (250, 250)}, verbose_name='imagem do local')),
            ],
        ),
    ]
