from django.db import models
class NewCustomer(models.Model):
    customer_name=models.CharField(max_length=20,)
    company_name=models.CharField(max_length=50)
    customer_display_name=models.CharField(max_length=100)
    customer_email=models.CharField(max_length=20,unique=True)
    customer_phone=models.IntegerField()
    website=models.CharField(max_length=20)

    def __str__(self):
        return self.customer_name



