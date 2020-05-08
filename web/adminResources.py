from import_export import resources
from .models import Theme

class ThemeResource(resources.ModelResource):

    class Meta:
        model = Theme
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ('Seed', 'HumanTheme', 'WolfTheme')
