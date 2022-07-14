# Generated by Django 4.0.5 on 2022-07-14 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=400)),
                ('Company', models.CharField(max_length=400)),
                ('website', models.URLField()),
                ('location', models.CharField(max_length=500)),
                ('skill', models.CharField(max_length=400)),
                ('bio', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
