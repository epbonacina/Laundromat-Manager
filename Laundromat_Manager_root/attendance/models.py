from django.db import models


class Employee (models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=150)
    password = models.CharField(max_length=250)
    role = models.CharField(max_length=2, choices=[("MG", "Manager"), ("RC", "Receptionist")])

class Client (models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=150)
    street_name = models.CharField(max_length=150)
    street_number = models.SmallIntegerField()
    CPF = models.CharField(max_length=14, blank=True)


class FinalReceipt (models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    client_id = models.ForeignKey(Client, on_delete=models.PROTECT)
    creation_date = models.DateTimeField(auto_now_add=True)
    total = models.FloatField()


class Item (models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=150)
    price = models.FloatField()


class KgItem (models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=150)
    price_per_kg = models.FloatField()


class ReceiptItem (models.Model):
    final_receipt_id = models.ForeignKey(FinalReceipt, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.PROTECT)
    qtt = models.IntegerField()
    total = models.FloatField()
    description = models.TextField()


class ReceiptKgItem (models.Model):
    final_receipt_id = models.ForeignKey(FinalReceipt, on_delete=models.CASCADE)
    kg_item_id = models.ForeignKey(KgItem, on_delete=models.PROTECT)
    weight = models.FloatField()
    total = models.FloatField()
    description = models.TextField()


# Create your models here.
