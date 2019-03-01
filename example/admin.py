# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Training, Exercise, TE

# Register your models here.
admin.site.register(Training)
admin.site.register(Exercise)
admin.site.register(TE)

