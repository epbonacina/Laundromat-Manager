# Generated by Django 4.0.4 on 2022-05-06 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('street_name', models.CharField(max_length=150)),
                ('street_number', models.SmallIntegerField()),
                ('CPF', models.CharField(blank=True, max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='KgItem',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('price_per_kg', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('total', models.FloatField()),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='attendance.client')),
            ],
        ),
        migrations.CreateModel(
            name='ReceiptKgItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('total', models.FloatField()),
                ('description', models.TextField()),
                ('kg_item_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='attendance.kgitem')),
                ('receipt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.receipt')),
            ],
        ),
        migrations.CreateModel(
            name='ReceiptItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtt', models.IntegerField()),
                ('total', models.FloatField()),
                ('description', models.TextField()),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='attendance.item')),
                ('receipt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.receipt')),
            ],
        ),
    ]
