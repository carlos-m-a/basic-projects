from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from .models import Profile, Setting

User = get_user_model()

class NewUserAdmin(UserAdmin):
    readonly_fields = ["date_joined", "last_login", "profile", "setting"]
    add_fieldsets = (
            (
                None,
                {
                    'classes': ('wide',),
                    'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2'),
                },
            ),
        )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (_("Profile and settings"), {"fields": ("profile", "setting")})
    )

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False


class AccountsBaseAdmin(admin.ModelAdmin):
    readonly_fields = ["user",]
    search_fields = ["user__username", "user__email", "user__first_name", "user__last_name"]

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False
    def has_add_permission(self, request):
        return False


admin.site.register(User, NewUserAdmin)
admin.site.register(Profile, AccountsBaseAdmin)
admin.site.register(Setting, AccountsBaseAdmin)