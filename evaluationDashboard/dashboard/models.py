from django.db import models

# Create your models here.
class UploadTable(models.Model):
    file = models.FileField(upload_to="documents/")

class UploadTSV(models.Model):
    data = models.JSONField()