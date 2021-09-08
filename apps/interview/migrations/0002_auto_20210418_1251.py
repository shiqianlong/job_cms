# Generated by Django 3.2 on 2021-04-18 04:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interview', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidate',
            options={'permissions': [('export', 'Can export candidate list'), ('notify', 'notify interviewer for candidate review')], 'verbose_name': '应聘者', 'verbose_name_plural': '应聘者'},
        ),
        migrations.AlterField(
            model_name='candidate',
            name='first_interviewer_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_interviewer_user', to=settings.AUTH_USER_MODEL, verbose_name='一面官'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='second_interviewer_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_interviewer_user', to=settings.AUTH_USER_MODEL, verbose_name='二面官'),
        ),
    ]