from django.contrib import admin
from .models import Events
from .models import urd
# Register your models here.
class UrdAdmin(admin.ModelAdmin):
    list_display=['name','emailid','collegename','semester','mobilenum','events']
    list_filter=(['events'])
class EventsAdmin(admin.ModelAdmin):
    list_display=['name','desc']
admin.site.register(urd,UrdAdmin)
admin.site.register(Events,EventsAdmin)
