# Generated by Django 3.1.5 on 2021-02-15 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_customer_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='customer',
            new_name='user',
        ),
    ]