# Generated by Django 4.0.5 on 2022-07-10 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pic',
            field=models.ImageField(default='profile.jpg', upload_to=''),
            preserve_default=False,
        ),
    ]