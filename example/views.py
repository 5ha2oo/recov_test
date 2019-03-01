# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Training, Exercise, TE


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        trainings = Training.objects.all();
        context['trainings'] = trainings;
        context['exercise'] = Exercise.objects.all()
        context['data'] = TE.objects.filter(training__in=trainings).select_related()
        return context


class PatientView(TemplateView):
    template_name = 'index.html'
