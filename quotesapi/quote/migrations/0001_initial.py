# Generated by Django 4.0.6 on 2022-07-09 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_body', models.CharField(max_length=250)),
                ('context', models.CharField(max_length=250)),
                ('source', models.URLField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('quote_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
