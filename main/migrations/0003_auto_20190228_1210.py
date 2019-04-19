# Generated by Django 2.1.7 on 2019-02-28 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190227_1244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='message',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='relates_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Message'),
        ),
        migrations.AddField(
            model_name='training',
            name='user_done',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]