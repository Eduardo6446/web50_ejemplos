from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Category, SubCategory, Product
# Import necessary classes from unfold and django.contrib.auth

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass
    

# Register your models here.
@admin.register(Category)
class CustomAdminClass(ModelAdmin):
    pass


@admin.register(SubCategory)
class CustomAdminClass(ModelAdmin):
    pass

@admin.register(Product)
class CustomAdminClass(ModelAdmin):
    pass