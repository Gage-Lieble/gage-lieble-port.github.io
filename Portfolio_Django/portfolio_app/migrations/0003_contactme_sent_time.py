# Generated by Django 4.0.3 on 2022-04-20 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_alter_contactme_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactme',
            name='sent_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]