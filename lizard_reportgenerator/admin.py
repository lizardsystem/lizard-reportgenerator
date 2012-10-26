from django.contrib import admin
from lizard_reportgenerator.models import GeneratedReport
from lizard_reportgenerator.models import ReportTemplate
from lizard_security.admin import SecurityFilteredAdmin


class GeneratedReportInline(admin.TabularInline):
    model = GeneratedReport


class ReportTemplateAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'slug',
                    'kind',
                    'generation_module',
                    'generation_function',
                    'extra_arguments',
                    'rtf_support',
                    'doc_support',
                    'pdf_support',
                    'csv_support',
                    'xls_support')


class GeneratedReportAdmin(SecurityFilteredAdmin):
    list_display = ('rtf_document',
                    'pdf_document',
                    'template',
                    'area',
                    'generated_on',
                    'visible')


admin.site.register(ReportTemplate, ReportTemplateAdmin)
admin.site.register(GeneratedReport, GeneratedReportAdmin)
