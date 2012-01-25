# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.db import models
import datetime 

# Create your models here.
from lizard_area.models import Area
from lizard_security.models import DataSet
from lizard_security.manager import FilteredManager

REPORT_TEMPLATE_TYPES = (
    ('algemeen', u'Algemeen'),
    ('krw', u'KRW'),
    ('aan_afvoer', u'Aan/afvoer'),
)

class ReportTemplate(models.Model):
    """(ReportTemplate description)"""
    name = models.CharField(blank=False, max_length=255)
    kind = models.CharField(
        blank=False,
        choices=REPORT_TEMPLATE_TYPES, 
        max_length=255, 
        null=False, 
        default="algemeen")
        
    def __unicode__(self):
        return str(self.name)


class GeneratedReport(models.Model):
    document_rtf = models.CharField(blank=False, max_length=255) # Stores filenames
    document_pdf = models.CharField(blank=False, max_length=255) # Stores filenames
    template = models.ForeignKey(ReportTemplate)
    area = models.ForeignKey(Area)
    generated_on = models.DateTimeField(blank=True, default=datetime.datetime.now)
    data_set = models.ForeignKey(DataSet, blank=True, null=True)
    visible = models.BooleanField(default=True)    
    supports_object_permissions = True
    objects = FilteredManager()

    def __unicode__(self):
        return str(self.template.name)
