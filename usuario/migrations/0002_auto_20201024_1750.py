# Generated by Django 3.1.2 on 2020-10-24 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interprete',
            name='avatar',
            field=models.ImageField(default='avatars/no-img.jpg', upload_to='images/avatars/'),
        ),
    ]
