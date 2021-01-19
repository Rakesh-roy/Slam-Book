from django.contrib import admin
from Friends.models import SlamBook

@admin.register(SlamBook)
class ViewAdmin(admin.ModelAdmin):
    readonly_fields = ('slam_no',)



