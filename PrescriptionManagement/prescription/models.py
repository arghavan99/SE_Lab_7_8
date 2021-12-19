from django.db import models


class Prescription(models.Model):
    doctor_id = models.IntegerField()
    patient_n_id = models.CharField(max_length=10)
    drug_list = models.TextField(max_length=1000)
    comment = models.CharField(max_length=100, null=True, blank=True)