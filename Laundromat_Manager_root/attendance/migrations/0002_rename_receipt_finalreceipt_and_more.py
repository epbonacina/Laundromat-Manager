# Generated by Django 4.0.4 on 2022-05-06 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Receipt',
            new_name='FinalReceipt',
        ),
        migrations.RenameField(
            model_name='receiptitem',
            old_name='receipt_id',
            new_name='final_receipt_id',
        ),
        migrations.RenameField(
            model_name='receiptkgitem',
            old_name='receipt_id',
            new_name='final_receipt_id',
        ),
    ]
