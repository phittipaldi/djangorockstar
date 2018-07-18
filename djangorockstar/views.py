# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.base import RedirectView


class IndexRedirectView(RedirectView):

    permanent = False
    query_string = True
    pattern_name = 'event:event-list'

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)
