# Generated by Django 4.2.6 on 2024-12-28 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invista_me', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investimento',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]