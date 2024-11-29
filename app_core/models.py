from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name="Created At",
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated At",
        auto_now=True
    )

    class Meta:
        abstract = True
