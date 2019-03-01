# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

CHAR_MAX_LENGTH = 256
# Create your models here.


class Training(models.Model):
    date = models.DateTimeField()
    description = models.CharField(max_length=256, default="")

    def __str__(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S")


class Exercise(models.Model):
    type = models.CharField(max_length=CHAR_MAX_LENGTH, default="")
    name = models.CharField(max_length=CHAR_MAX_LENGTH, default="")
    description = models.CharField(max_length=256, default="")

    def __str__(self):
        return self.name


class TE(models.Model):
    training = models.ForeignKey(Training, on_delete=models.SET_NULL, null=True, blank=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.SET_NULL, null=True, blank=True)
