# Generated by Django 2.1.7 on 2019-09-10 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190910_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(default='/noprofile.png', null=True, upload_to='images/'),
        ),
    ]