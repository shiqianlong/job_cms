# Generated by Django 3.2 on 2021-04-08 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_resume_apply_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='gender',
            field=models.CharField(blank=True, choices=[('男', '男'), ('女', '女')], default='男', max_length=100, verbose_name='性别'),
        ),
    ]
