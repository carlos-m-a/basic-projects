from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from .models import Profile, Setting

User = get_user_model()

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Campos visibles en la lista
    list_display = (
        'public_id',
        'email',
        'username',
        'is_active',
        'is_sso_only',
        'is_managed',
        'is_deleted',
        'date_joined',
    )

    # Filtros laterales
    list_filter = (
        'is_deleted',
        'is_active',
        'is_sso_only',
        'is_managed',
        'is_staff',
        'is_superuser',
        'groups',
    )

    # Búsqueda
    search_fields = ('public_id', 'email', 'username', 'phone_number')
    ordering = ('-date_joined',)

    # Formulario de edición
    fieldsets = (
        (_('Identifiers'), {'fields': ('public_id', 'email', 'password')}),
        (_('Personal info'), {'fields': ('username', 'first_name', 'last_name', 'phone_number')}),
        (_('B2B Configuration'), {'fields': ('is_sso_only', 'is_managed')}),
        (_('Permissions & Status'), {
            'fields': ('is_active', 'is_deleted', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined', 'updated_at', 'created_at')}),
    )

    # Campos que no se pueden editar manualmente
    readonly_fields = ('public_id', 'date_joined', 'updated_at', 'created_at')

    # Formulario de creación
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )

    actions = ['deactivate_users', 'reactivate_users', 'soft_delete_users', 'restore_users']

    # Acciones masivas
    @admin.action(description=_("Deactivate selected users"))
    def deactivate_users(self, request, queryset):
        for user in queryset:
            user.deactivate()
        self.message_user(request, "Usuarios desactivados.")

    @admin.action(description=_("Reactivate selected users"))
    def reactivate_users(self, request, queryset):
        for user in queryset:
            user.reactivate()
        self.message_user(request, "Usuarios reactivados.")

    @admin.action(description=_("Soft-delete selected users"))
    def soft_delete_users(self, request, queryset):
        queryset.update(is_deleted=True)
        self.message_user(request, "Usuarios marcados como eliminados.")

    @admin.action(description=_("Restore selected users"))
    def restore_users(self, request, queryset):
        queryset.update(is_deleted=False)
        self.message_user(request, "Usuarios restaurados.")


class AccountsBaseAdmin(admin.ModelAdmin):
    readonly_fields = ["user",]
    search_fields = ["user__username", "user__email", "user__first_name", "user__last_name"]

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False
    def has_add_permission(self, request):
        return False


admin.site.register(Profile, AccountsBaseAdmin)
admin.site.register(Setting, AccountsBaseAdmin)