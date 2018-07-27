from .logentrys import LogEntryAdmin
from django.contrib.admin.models import LogEntry
from django.contrib import admin


admin.site.register(LogEntry, LogEntryAdmin)
