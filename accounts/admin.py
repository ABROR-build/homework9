from django.contrib import admin
from . import models


class ConfAdmin(admin.ModelAdmin):
    list_display = ['username', 'age', 'bio', 'date_joined', 'isblogger']


admin.site.register(models.Accounts, ConfAdmin)
