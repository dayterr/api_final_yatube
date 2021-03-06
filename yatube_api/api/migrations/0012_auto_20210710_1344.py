# Generated by Django 2.2.6 on 2021-07-10 13:44

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210710_1342'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='team_home_and_team_visitors_can_not_be_equal',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, user=django.db.models.expressions.F('following')), name='Подписчик и подписант должны быть разными людьми'),
        ),
    ]
