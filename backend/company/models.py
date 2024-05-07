from django.db import models
from utils.models import CommonInfo


class ComapanyModel(CommonInfo):
    name = models.CharField(max_length=32, unique=True)
    title = models.CharField(max_length=55, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    located = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        db_table = "company"
