# Generated by Django 2.1.7 on 2019-02-27 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advice',
            name='score',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='user_score',
            field=models.IntegerField(null=True),
        ),
    ]