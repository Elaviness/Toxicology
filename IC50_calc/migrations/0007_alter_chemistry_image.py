# Generated by Django 3.2 on 2021-05-06 11:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('IC50_calc', '0006_auto_20210506_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemistry',
            name='image',
            field=models.BinaryField(default=None, null=True),
        ),
    ]
