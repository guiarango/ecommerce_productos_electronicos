# Generated by Django 3.0.1 on 2022-12-06 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
