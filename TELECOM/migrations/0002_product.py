# Generated by Django 4.2.7 on 2023-11-13 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TELECOM', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(default='product')),
                ('origin', models.CharField(default='kenya', max_length=50)),
                ('color', models.CharField(default='white', max_length=30)),
            ],
        ),
    ]
