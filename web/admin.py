from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .adminResources import ThemeResource
from web.models import Theme

#admin.site.register(Theme)

@admin.register(Theme)
class ThemeAdmin(ImportExportModelAdmin):
    resource_class = ThemeResource

