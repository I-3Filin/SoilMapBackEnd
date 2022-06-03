from django.contrib.gis.db import models
import uuid


class CesiumActivity(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Activity = models.FileField()
    Depth = models.IntegerField()
    SamplingDate = models.DateTimeField()
    SamplingMethods = {
        (1, 'Послойный'),
        (2, 'Точечный'),
        (2, 'Объедененный')
    }
    SamplingMethod = models.IntegerField(choices=SamplingMethods)
    SoilFlushing = models.IntegerField()
    Geom = models.PointField()

