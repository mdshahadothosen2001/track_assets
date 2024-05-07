from django.db import models

from utils.models import CommonInfo
from company.models import ComapanyModel


class DeviceModel(CommonInfo):
    company = models.ForeignKey(ComapanyModel, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=32)
    model = models.CharField(max_length=32, null=True, blank=True)
    handed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} : {self.model}"

    class Meta:
        verbose_name = "Device"
        verbose_name_plural = "Devices"
        db_table = "device"
