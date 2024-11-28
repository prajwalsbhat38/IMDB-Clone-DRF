from django.contrib import admin
from .models import StreamingPlatform, WatchList, Reviews

# Register your models here.
admin.site.register(StreamingPlatform)
admin.site.register(WatchList)
admin.site.register(Reviews)