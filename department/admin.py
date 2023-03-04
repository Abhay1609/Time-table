from django.contrib import admin
from .models import *
admin.site.register(Department)
admin.site.register(Subject)

# Register your models here.
@admin.register(Lecture)
class lectureAdmin(admin.ModelAdmin):
    list_display = ['year','branche','section','faculty','subject','time']