from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User



class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'



class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_moderator', 'is_blocked')


    def is_moderator(self, obj):
        if hasattr(obj, 'profile'):
            return obj.profile.is_moderator
        return False

    is_moderator.boolean = True
    is_moderator.short_description = 'Moderator'

    def is_blocked(self, obj):
        if hasattr(obj, 'profile'):
            return obj.profile.is_blocked
        return False

    is_blocked.boolean = True
    is_blocked.short_description = 'Blocked'


# Отменяем регистрацию стандартного User и регистрируем с кастомным админом
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

