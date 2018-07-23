# -*- encoding: utf-8 -*-
from django.views.generic import RedirectView
from django.contrib.auth import views


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/accounts/login/'

    def get(self, request, *args, **kwargs):
        views.logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
