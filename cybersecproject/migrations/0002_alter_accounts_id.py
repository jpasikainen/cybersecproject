# Generated by Django 3.2.3 on 2021-06-03 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cybersecproject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]