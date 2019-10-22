from django.contrib.auth.models import User, Group
from django.contrib import admin
from .models import Kingdom, Battle

admin.site.register(Kingdom)

@admin.register(Battle)
class BattleAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False






admin.site.unregister(Group)
admin.site.unregister(User)