# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView


class IndexEvent(TemplateView):
    template_name = "index_event.html"

    def get_context_data(self, **kwargs):
        context = super(IndexEvent, self).get_context_data(**kwargs)
        return context
