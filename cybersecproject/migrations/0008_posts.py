# Generated by Django 3.2.3 on 2021-06-03 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cybersecproject', '0007_auto_20210603_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=10)),
                ('body', models.CharField(max_length=300)),
            ],
        ),
    ]