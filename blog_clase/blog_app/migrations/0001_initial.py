# Generated by Django 3.1.5 on 2021-01-07 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publicado')),
                ('body', models.TextField()),
                ('publicado', models.DateTimeField(default=django.utils.timezone.now)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('estado', models.CharField(choices=[('privado', 'Privado'), ('publico', 'Publico')], default='publico', max_length=11)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='NutriPPer_app_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-publicado',),
            },
        ),
    ]
