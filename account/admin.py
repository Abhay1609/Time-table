from django.contrib import admin
from account.models import User
from department.models import Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.


class UserModelAdmin(BaseUserAdmin):
 

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ('id','email','mobile_number', 'full_name','isverified', 'is_admin')
    list_filter = ('is_admin','isverified')
    fieldsets = (
        ('User Credentials', {'fields': ('mobile_number','email', 'password')}),
        ('Personal info', {'fields': ('full_name','age','isverified','gender')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mobile_number','email', 'full_name','age','gender','isverified', 'password1'),
        }),
    )
    search_fields = ('email','id','mobile_number')
    ordering = ('id',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)
admin.site.register(Profile)
# Register your models here.
