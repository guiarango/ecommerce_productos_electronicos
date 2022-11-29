# Generated by Django 4.1.2 on 2022-11-27 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fundador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=100)),
                ('historia', models.TextField(max_length=500)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='fundador/')),
            ],
        ),
    ]
