# Generated by Django 3.2 on 2021-05-08 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IC50_calc', '0008_alter_chemistry_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smile', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='IC50_calc/img/search')),
                ('flag', models.BooleanField()),
                ('ic50', models.FloatField()),
            ],
        ),
    ]