# Generated by Django 3.1.5 on 2021-02-18 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20210217_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='static/images/placeholder.png', null=True, upload_to=''),
        ),
    ]
