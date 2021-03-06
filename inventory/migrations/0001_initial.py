# Generated by Django 2.0.2 on 2018-03-12 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_id', models.CharField(default='', max_length=10)),
                ('current_id', models.CharField(default='', max_length=10)),
                ('name', models.CharField(default='', max_length=10)),
                ('material', models.CharField(default='', max_length=10)),
                ('color', models.CharField(default='', max_length=10)),
                ('size', models.CharField(default='', max_length=10)),
                ('unit', models.CharField(default='', max_length=10)),
                ('unit_price', models.IntegerField(default=0)),
                ('cost', models.IntegerField(default=0)),
                ('default_price', models.IntegerField(default=0)),
                ('remarks', models.CharField(default='', max_length=256)),
                ('price_coff', models.FloatField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10)),
                ('tel', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_id', models.CharField(default='', max_length=10)),
                ('number', models.IntegerField(default=0)),
                ('purchase_date', models.DateTimeField(verbose_name='date purchased')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Product')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Provider')),
            ],
        ),
    ]
