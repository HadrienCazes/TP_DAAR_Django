# Generated by Django 3.1.7 on 2021-03-01 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytig', '0002_auto_20201204_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProduitDisponible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tigID', models.IntegerField(default='-1')),
            ],
            options={
                'ordering': ('tigID',),
            },
        ),
    ]
