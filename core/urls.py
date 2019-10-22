from django.contrib import admin
from django.urls import path
from showsapp.admin import shows_admin_site


urlpatterns = [
    path('admin/', admin.site.urls),
    path('shows-admin/', shows_admin_site.urls),
]
admin.site.site_header = "Rulers"
admin.site.index_title = "Ruler Administration"
admin.site.site_title = "Great Rulers"