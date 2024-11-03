from .models import Bill, Payment
from rest_framework import serializers

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ["id", "service_name", "logo", "last_paid_date", "next_due_date", "amount_due", "recurring"]
        
        
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["id", "bill", "amount_paid", "date_paid"]