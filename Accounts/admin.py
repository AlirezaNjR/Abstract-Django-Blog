from django.contrib import admin
from .models import CustomUserModel
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm , CustomUserCreationForm
#Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUserModel
    add_form = CustomUserCreationForm
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('image','instagram','telegram','site','bio')}),
    )
    
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('image','instagram','telegram','site','bio')}),
    )
    
admin.site.register(CustomUserModel,CustomUserAdmin)