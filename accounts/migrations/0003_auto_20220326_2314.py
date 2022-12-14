# Generated by Django 3.1.13 on 2022-03-26 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220326_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='aadhar_number',
            field=models.CharField(default=912, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='is_valid_policy_id',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='policy_id',
            field=models.CharField(default=12112312, max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
