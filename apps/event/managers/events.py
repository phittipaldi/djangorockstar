from django.db import models
from datetime import datetime


class EventManager(models.Manager):

    def all_active_events(self):
        current_date = datetime.now().replace(hour=23, minute=59)
        return self.filter(is_active=True,
                           end_date__gte=current_date)
