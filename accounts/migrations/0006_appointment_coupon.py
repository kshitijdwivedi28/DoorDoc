# Generated by Django 3.1.13 on 2022-03-26 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='coupon',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
    ]