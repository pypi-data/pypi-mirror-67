from django.db import models


class CSVUploadModel(models.Model):
    csv_upload_compulsory_fields = []  # list of optional field in model that you want to treat as compulsory during csv upload
    fk_handle_by_id = []  # a list of fk fields that needs to be handled by id inside csv file

    class Meta:
        abstract = True
