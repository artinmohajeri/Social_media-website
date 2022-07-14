# Generated by Django 4.0.5 on 2022-07-14 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_delete_register_alter_user_location_alter_user_pic'),
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
            ],
        ),
    ]
