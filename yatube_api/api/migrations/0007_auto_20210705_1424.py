# Generated by Django 2.2.6 on 2021-07-05 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210704_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание сообщества'),
        ),
    ]
