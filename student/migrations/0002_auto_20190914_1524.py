# Generated by Django 2.2.5 on 2019-09-14 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='img',
            field=models.ImageField(default='images/profile-2398782_960_720_ZjcWbXL.png', upload_to='images/'),
        ),
    ]