# Generated by Django 4.1.4 on 2022-12-25 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0007_remove_homespecified_date_remove_homespecified_time_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='home',
            options={'ordering': ['-pk']},
        ),
        migrations.AddField(
            model_name='home',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
    ]