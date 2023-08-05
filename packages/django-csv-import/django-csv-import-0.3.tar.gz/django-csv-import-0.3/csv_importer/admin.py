from django.contrib import admin

# Register your models here.
from csv_importer.models import CSVUploadModel


class CsvUploadAdmin(admin.ModelAdmin):
    allow_csv_upload = True

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        if not isinstance(model(), CSVUploadModel):
            raise NotImplementedError("model must an instance of CSVUploadModel")

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['allow_csv_upload'] = self.allow_csv_upload
        return super().changelist_view(
            request, extra_context=extra_context,
        )
