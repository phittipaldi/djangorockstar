from django.db import models
from django.contrib.auth.models import User


class LogMail(models.Model):
    subject = models.CharField(max_length=64)
    to = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return ''.format(self.subject)
