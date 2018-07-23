# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"
