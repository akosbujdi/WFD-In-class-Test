from django.db import models


# Create your models here.
class Salesperson(models.Model):
    Salesperson_ID = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)


class Car(models.Model):
    Car_ID = models.AutoField(primary_key=True)
    Serial_Number = models.CharField(max_length=50)
    Make = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)
    Colour = models.CharField(max_length=50)
    Year = models.IntegerField()
    Car_for_sale = models.BooleanField(default=False)


class Customer(models.Model):
    Customer_ID = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Phone_Number = models.CharField(max_length=20)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    Postal_Code = models.CharField(max_length=20)


class Service(models.Model):
    Service_ID = models.AutoField(primary_key=True)
    Serivce_Name = models.CharField(max_length=50)
    Hourly_Rate = models.FloatField()


class Parts(models.Model):
    Parts_ID = models.AutoField(primary_key=True)
    Part_Number = models.IntegerField()
    Description = models.TextField()
    Purchase_Price = models.FloatField()
    Retail_Price = models.FloatField()


class Service_Ticket(models.Model):
    Service_Ticket_ID = models.AutoField(primary_key=True)
    Service_Ticket_Number = models.IntegerField(unique=True)
    Car_ID = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    Date_Received = models.DateField()
    Comments = models.TextField()
    Date_Returned = models.DateField()


class Parts_Used(models.Model):
    Parts_Used_ID = models.AutoField(primary_key=True)
    Part_ID = models.ForeignKey(Parts, on_delete=models.CASCADE)
    Service_Ticket_ID = models.ForeignKey(Service_Ticket, on_delete=models.CASCADE, null=True)
    Number_Used = models.IntegerField()
    Price = models.FloatField()


class Mechanic(models.Model):
    Mechanic_ID = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)


class Sales_Invoice(models.Model):
    Invoice_ID = models.AutoField(primary_key=True)
    invoice_no = models.IntegerField(unique=True)
    date = models.DateField()
    Salesperson_ID = models.ForeignKey(Salesperson, on_delete=models.CASCADE)
    Car_ID = models.OneToOneField(Car, on_delete=models.CASCADE, null=True)
    Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)


class Service_Mechanic(models.Model):
    Service_Mechanic_ID = models.AutoField(primary_key=True)
    Service_Ticked_ID = models.ForeignKey(Service_Ticket, on_delete=models.CASCADE)
    Service_ID = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    Mechanic_ID = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    Hours = models.IntegerField()
    Comment = models.TextField()
    Rate = models.FloatField()
