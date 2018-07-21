# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from apps.utils import initial_data


class Command(BaseCommand):
    def handle(self, *args, **option):
        initial_data.data_default_event()
