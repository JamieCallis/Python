# Generated by Django 2.1.5 on 2019-03-31 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0004_bookmetadata_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktext',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
