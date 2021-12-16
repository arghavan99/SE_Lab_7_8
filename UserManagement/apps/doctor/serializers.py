from rest_framework import serializers

class DoctorSerializer(serializers.Serializer):
    national_id = serializers.CharField()
    name = serializers.CharField()
