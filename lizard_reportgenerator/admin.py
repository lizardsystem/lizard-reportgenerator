from django.contrib import admin
from lizard_reportgenerator.models import GeneratedReport
from lizard_reportgenerator.models import ReportTemplate
from lizard_security.admin import SecurityFilteredAdmin


class GeneratedReportInline(admin.TabularInline):
    model = GeneratedReport

class ReportTemplateAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [
        GeneratedReportInline
    ]

class GeneratedReportAdmin(SecurityFilteredAdmin):
    list_display = ('document_rtf', 'document_pdf', 'template', 'area', 'generated_on', 'visible')
    



admin.site.register(ReportTemplate, ReportTemplateAdmin)
admin.site.register(GeneratedReport, GeneratedReportAdmin)
