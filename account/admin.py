from django.contrib import admin
from account.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import lecture
# Register your models here.


class UserModelAdmin(BaseUserAdmin):
 

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ('id','email','mobile_number', 'full_name','isverified', 'is_admin','department')
    list_filter = ('is_admin','isverified','department','subject')
    fieldsets = (
        ('User Credentials', {'fields': ('mobile_number','email', 'password')}),
        ('Personal info', {'fields': ('full_name','department','subject','age','isverified','gender')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mobile_number','email', 'full_name','age','gender','isverified','department','subject', 'password1'),
        }),
    )
    search_fields = ('email','id','mobile_number','department','subject')
    ordering = ('id',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)
# Register your models here.
@admin.register(lecture)
class lectureAdmin(admin.ModelAdmin):
    list_display = ['year','branche','section','faculty','subject','time']