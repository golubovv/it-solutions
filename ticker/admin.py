from django.contrib import admin

from .models import Ticker, Font

admin.site.register(Ticker)
admin.site.register(Font)