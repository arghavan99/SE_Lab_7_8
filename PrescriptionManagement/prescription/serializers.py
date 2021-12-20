from rest_framework import serializers


class PrescriptionSerializer(serializers.Serializer):
    doctor_id = serializers.IntegerField()
    patient_n_id = serializers.CharField()
    drug_list = serializers.CharField()
    comment = serializers.CharField()
