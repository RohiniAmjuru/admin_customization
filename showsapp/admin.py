from django.contrib.admin import AdminSite, ModelAdmin
from .models import Kid, Teen

class ShowsAdminSite(AdminSite):
    site_header = "Shows"
    site_title = "Shows Administration"
    index_title = "Shows Administration"


shows_admin_site = ShowsAdminSite(name='shows_admin')
shows_admin_site.register(Kid)
shows_admin_site.register(Teen)
