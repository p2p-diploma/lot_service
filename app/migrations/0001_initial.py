# Generated by Django 4.0.4 on 2022-05-12 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(max_length=200)),
                ('seller_id', models.CharField(max_length=200, unique=True)),
                ('price', models.FloatField()),
                ('buyer_id', models.CharField(blank=True, default=None, max_length=200, null=True)),
            ],
        ),
    ]
