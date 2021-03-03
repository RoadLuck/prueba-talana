from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.
class CustomUserAdmin(UserAdmin):
    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = models.User
    
    ordering = ('email',)
    list_display = ['pk','first_name', 'last_name', 'email']
    search_fields = ('email',)
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name','password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email','password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    ordering = ('email',)

admin.site.register(models.User, CustomUserAdmin)


from django.contrib import admin
from . import models
# Register your models here.



@admin.register(models.Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['user', 'token']
