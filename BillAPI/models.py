from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/', blank=True)
    last_paid_date = models.DateField(blank=True, null=True)
    next_due_date = models.DateField()
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    recurring = models.BooleanField()
    
    
    def __str__(self):
        return f"{self.service_name} - {self.user.username}"
    
    
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Payment for {self.user.username} - in amount of {self.amount_paid}"
