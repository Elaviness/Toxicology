# Generated by Django 3.2 on 2021-05-06 09:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('IC50_calc', '0002_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='img/mols'),
        ),
    ]
