# Generated by Django 4.0.5 on 2022-07-10 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='job',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
