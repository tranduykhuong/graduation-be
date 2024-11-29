from django.db import models

from app_core.models import BaseModel

class Wisher(BaseModel):
    yes = "yes"
    no = "no"
    unknown = "unknown"
    STATUS_CHOICES = [
        (yes, "yes"),
        (no, "no"),
        (unknown, "unknown"),
    ]

    key = models.CharField(
        verbose_name="Key",
        max_length=128,
        blank=True,
        null=True,
    )

    name = models.CharField(
        max_length=128,
        blank=True,
        null=True
    )

    last3phone = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    email = models.EmailField(
        max_length=128,
        blank=True,
        null=True
    )

    relationship = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    img_url = models.URLField(
        verbose_name="Img Url",
        max_length=256,
        blank=True,
        null=True
    )

    wisher = models.CharField(
        max_length=1028,
        blank=True,
        null=True
    )

    confirm = models.CharField(
        choices=STATUS_CHOICES,
        max_length=50,
        default=yes,
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        verbose_name="Is Active?",
        default=True
    )

    def __str__(self):
        return f'{self.name}'
