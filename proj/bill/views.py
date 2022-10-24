from django.shortcuts import render
from django.db import transaction
from django.db.models import F
from django.db.utils import OperationalError
from rest_framework.decorators import api_view
from rest_framework.response import Response

from bill.models import Bill
from bill.serializers import TransferSerilizer
from time import sleep
import logging

logger = logging.getLogger(__name__)

@api_view(["POST"])
def transfer(request):
    deserialized = TransferSerilizer(data=request.data)
    deserialized.is_valid(raise_exception=True)
    try:
        with transaction.atomic():
            Bill.objects.filter(id=deserialized.validated_data["from_bill"]).update(amount=F("amount") - deserialized.validated_data["amount"])
            bill = Bill.objects.filter(id=deserialized.validated_data["from_bill"]).first()
            sleep(deserialized.validated_data["seconds"])
            Bill.objects.filter(id=deserialized.validated_data["to_bill"]).update(amount=F("amount") + deserialized.validated_data["amount"])
    except OperationalError as e:
        logger.error(f"Deadlock error {e}")
    return Response("ok")

# @transaction.atomic
# @api_view(["POST"])
# def transfer(request):
#     deserialized = TransferSerilizer(data=request.data)
#     deserialized.is_valid(raise_exception=True)

#     Bill.objects.filter(id=deserialized.validated_data["from_bill"]).update(amount=F("amount") - deserialized.validated_data["amount"])
#     bill = Bill.objects.filter(id=deserialized.validated_data["from_bill"]).first()
#     bill.amount
#     sleep(deserialized.validated_data["seconds"])
#     Bill.objects.filter(id=deserialized.validated_data["to_bill"]).update(amount=F("amount") + deserialized.validated_data["amount"])
#     return Response("ok")

# Bill.objects.filter(id=1).update(amount=F("amount") - 50)