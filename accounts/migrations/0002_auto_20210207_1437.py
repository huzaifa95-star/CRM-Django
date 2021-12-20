# Generated by Django 3.1.5 on 2021-02-07 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('out of delivery', 'out of delivery'), ('delivered', 'delivered')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('category', models.CharField(max_length=200, null=True)),
                ('date_ordered', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Cutomers',
            new_name='Cutomer',
        ),
    ]