# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from . import models


class IndexEvent(TemplateView):
    template_name = "index_event.html"

    def get_context_data(self, **kwargs):
        context = super(IndexEvent, self).get_context_data(**kwargs)

        if self.kwargs.get('uuid'):
            context['event'] = models.Event.objects.get(
                uuid=self.kwargs.get('uuid'))

        return context
