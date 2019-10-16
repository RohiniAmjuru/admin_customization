from django.contrib.auth.models import User, Group
from django.contrib import admin
from .models import Kingdom, Battle

admin.site.register(Kingdom)
admin.site.register(Battle)

admin.site.unregister(Group)
admin.site.unregister(User)