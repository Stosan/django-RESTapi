# Generated by Django 3.2.9 on 2021-11-26 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot_platform', '0002_alter_payloaddevice_seqnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payloaddevice',
            name='device',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
