from django.db import models
import uuid

# Create your models here.
# from django.db import models
from django.db import models


class TrainedModel(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    model_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    model_path = models.CharField(max_length=255, default=' ')
    model_for = models.CharField(max_length=255)
    accuracy = models.FloatField(null=True)
    rmse = models.FloatField(null=True)
    silhouette = models.FloatField(null=True)

    class Meta:
        db_table = 'trained_models'

    def __str__(self):
        return self.model_name
