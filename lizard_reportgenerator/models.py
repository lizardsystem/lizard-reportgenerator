# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.db import models
import datetime 

# Create your models here.
from lizard_area.models import Area
from lizard_security.models import DataSet
from lizard_security.manager import FilteredManager
from vss.settings import MEDIA_ROOT
import os

REPORT_TEMPLATE_TYPES = (
    ('algemeen', u'Algemeen'),
    ('krw', u'KRW'),
    ('aan_afvoer', u'Aan/afvoer'),
)

class ReportTemplate(models.Model):
    """(ReportTemplate description)"""
    name = models.CharField(blank=False, max_length=255)
    slug = models.SlugField(blank=False, null=False )
    kind = models.CharField(
        blank=False,
        choices=REPORT_TEMPLATE_TYPES, 
        max_length=255, 
        null=False, 
        default="algemeen")
    generation_module = models.CharField(
        max_length=255,
        default="lizard_",
        help_text="module where generation function can be found")
    generation_function = models.CharField(
        max_length=255,
        default="todo",
        help_text="function name for report generation. arguments for this function are Area, output format and extra arguments")
    extra_arguments = models.CharField(
        max_length=255,
        default="{}",
        help_text="json with extra arguments")
    rtf_support = models.BooleanField(
        default=False)
    pdf_support = models.BooleanField(
        default=False)
    csv_support = models.BooleanField(
        default=False)
    xls_support = models.BooleanField(
        default=False)

    class Meta:
        ordering = ('name', )

    def __unicode__(self):
        return str(self.name)


class GeneratedReport(models.Model):
    template = models.ForeignKey(ReportTemplate)
    area = models.ForeignKey(Area, blank=True, null=True)
    data_set = models.ForeignKey(DataSet, blank=True, null=True)

    rtf_document = models.CharField(default='', blank=True, max_length=255) # Stores filenames
    pdf_document = models.CharField(default='', blank=True, max_length=255) # Stores filenames
    csv_document = models.CharField(default='', blank=True, max_length=255) # Stores filenames
    xls_document = models.CharField(default='', blank=True, max_length=255) # Stores filenames

    generated_on = models.DateTimeField(blank=True, default=datetime.datetime.today())
    visible = models.BooleanField(default=True)    

    supports_object_permissions = True
    objects = FilteredManager()

    class Meta:
        ordering = ('-generated_on', 'template__name')

    def save_file(self, file_buffer, file_format, name):

        file_location = os.path.join('reportgenerator', str(self.data_set), "%s_-_%i.%s"%(name, self.id, file_format))
        setattr(self, file_format + '_document',file_location)
        full_file_location = os.path.join(MEDIA_ROOT, file_location)

        d = os.path.dirname(full_file_location)
        if not os.path.exists(d):
            os.makedirs(d)
        f = file(full_file_location, "w")
        file_buffer.seek(0)
        f.write(file_buffer.read())
        f.close()
        return True

    def get_file(self, file_format):

        file_location = getattr(self, file_format + '_document')
        full_file_location = os.path.join(MEDIA_ROOT, file_location)

        f = file(full_file_location, "r")
        return f.read()

    def __unicode__(self):
        return str(self.template.name)
