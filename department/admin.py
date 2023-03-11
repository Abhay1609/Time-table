from django.contrib import admin
from .models import *
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Branch)
admin.site.register(Time_Table_Creator)


# Register your models here.
@admin.register(Lecture)
class lectureAdmin(admin.ModelAdmin):
    list_display = ['cid','day','faculty','subject','period']

@admin.register(Class)
class lectureAdmin(admin.ModelAdmin):
    list_display = ['id','branch','section','class_id','lunch']