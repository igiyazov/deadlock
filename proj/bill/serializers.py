from rest_framework import serializers
from bill.models import Bill

class TransferSerilizer(serializers.Serializer):
    to_bill = serializers.IntegerField()
    from_bill = serializers.IntegerField()
    seconds = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=12, decimal_places=6)