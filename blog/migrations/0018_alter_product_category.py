# Generated by Django 3.2 on 2021-05-10 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Humanoids', 'Humanoids'), ('Consumer', 'Consumer'), ('Drones', 'Drones'), ('Education', 'Education'), ('Military', 'Military & Security')], max_length=25),
        ),
    ]
