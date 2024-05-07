from django.db import models

from utils.models import CommonInfo
from user.models import UserAccount
from device.models import DeviceModel


class AssignDeviceModel(CommonInfo):
    employee = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)
    device = models.ForeignKey(DeviceModel, on_delete=models.DO_NOTHING)
    taken_at = models.BooleanField(default=True)
    return_at = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee} : {self.device}"

    class Meta:
        verbose_name = "Assign Device"
        verbose_name_plural = "Assgn Devices"
        db_table = "assign_device"
