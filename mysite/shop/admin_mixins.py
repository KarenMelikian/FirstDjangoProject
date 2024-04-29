import csv

from django.db.models import QuerySet
from django.db.models.options import Options
from django.http import HttpRequest, HttpResponse


class ExportAsCSVMixin:
    """
    Mixin class to export queryset data as CSV.

    This mixin provides a method to export queryset data as a CSV file.

    Methods:
        export_csv(request: HttpRequest, queryset: QuerySet) -> HttpResponse:
            Exports the provided queryset data as a CSV file and returns an HTTP response.

    Attributes:
        None
    """
    def export_csv(self, request: HttpRequest, queryset: QuerySet):
        """
        Exports the provided queryset data as a CSV file.

        Args:
            request (HttpRequest): The HTTP request.
            queryset (QuerySet): The queryset to export as CSV.

        Returns:
            HttpResponse: The HTTP response containing the CSV data.
        """
        meta: Options = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta.model_name}-export.csv'

        csv_writer = csv.writer(response)
        csv_writer.writerow(field_names)

        for obj in queryset:
            csv_writer.writerow([getattr(obj, f) for f in field_names])

        return response

    export_csv.short_description = 'Export as CSV'
