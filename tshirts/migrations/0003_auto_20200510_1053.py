# Generated by Django 3.0.5 on 2020-05-10 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tshirts', '0002_auto_20200510_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tshirt',
            name='story',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tshirts.Story'),
        ),
    ]
