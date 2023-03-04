from django.contrib import admin
from .models import *
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Branch)


# Register your models here.
@admin.register(Lecture)
class lectureAdmin(admin.ModelAdmin):
    list_display = ['year','branch','section','faculty','subject','time']