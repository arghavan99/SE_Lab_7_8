from rest_framework import serializers

class PatientSerializer(serializers.Serializer):
    national_id = serializers.CharField()
    name = serializers.CharField()
