# Generated by Django 2.2.4 on 2019-08-28 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='complemento',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Complemento'),
        ),
    ]
