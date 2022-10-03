from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model

class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

    created = models.DateTimeField(editable=False, default=datetime.now)
    modified = models.DateTimeField(default=datetime.now)

    user = models.ForeignKey(get_user_model(), on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Category'


class Country(models.Model):
    name = models.CharField(max_length=100, null=True)

    created = models.DateTimeField(editable=False, default=datetime.now)
    modified = models.DateTimeField(default=datetime.now)

    user = models.ForeignKey(get_user_model(), on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Country'