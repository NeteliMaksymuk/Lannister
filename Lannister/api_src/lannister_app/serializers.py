from rest_framework import serializers
from .models import BonusRequest


class BonusRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BonusRequest
        fields = '__all__'


class BonusFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BonusRequest
        fields = ["id", "creator", "reviewer", "bonus_type", "description", "status"]


class BonusRequestHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BonusRequest
        fields = [
            "id",
            "date_created",
            "date_approved",
            "date_rejected",
            "date_done",
            "date_changed",
            "date_payment",
        ]
