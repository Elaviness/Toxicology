# Generated by Django 3.2 on 2021-05-06 11:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('IC50_calc', '0005_alter_image_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='chemistry',
            name='image',
            field=models.BinaryField(default=None),
        ),
    ]
