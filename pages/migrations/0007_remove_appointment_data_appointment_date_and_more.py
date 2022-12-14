# Generated by Django 4.0.6 on 2022-08-30 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_appointment_alter_contect_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='data',
        ),
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='datatime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contect',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
