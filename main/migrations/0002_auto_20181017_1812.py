# Generated by Django 2.1.2 on 2018-10-17 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitbituser',
            name='access_token',
            field=models.CharField(default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='fitbituser',
            name='expires_in',
            field=models.CharField(default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='fitbituser',
            name='refresh_token',
            field=models.CharField(default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='fitbituser',
            name='scope',
            field=models.CharField(default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='fitbituser',
            name='token_type',
            field=models.CharField(default='', max_length=512),
        ),
    ]
