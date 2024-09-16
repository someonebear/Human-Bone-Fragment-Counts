from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Element)
admin.site.register(Landmark)
admin.site.register(Entry)
admin.site.register(EntryGroup)
