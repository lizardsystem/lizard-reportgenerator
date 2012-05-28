# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.conf import settings
from lizard_area.models import Area
from lizard_reportgenerator.models import ReportTemplate
from lizard_reportgenerator.models import GeneratedReport
from lizard_security.models import DataSet

from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

import xlwt as excel
from StringIO import StringIO
import csv

from cgi import escape
import cStringIO as StringIO
import ho.pisa as pisa


def index(request, template='lizard_reportgenerator/index.html'):
    '''
        returns overview page of reports and historic pages


    '''

    #todo: make function less KRW specific

    aan_afvoergebied_id = request.GET.get('aan_afvoergebied', None)
    krw_gebied_id = request.GET.get('krw_waterlichaam', None)

    if request.user.is_superuser:
        data_sets = DataSet.objects.all()
    else:
        data_set_ids = getattr(request, 'ALLOWED_DATA_SET_IDS', None)
        data_sets = DataSet.objects.filter(id__in=data_set_ids)

    aan_afvoergebied = None
    krw_gebied = None

    try:
        aan_afvoergebied = Area.objects.get(ident=aan_afvoergebied_id)
    except Area.DoesNotExist:
        pass

    try:
        krw_gebied = Area.objects.get(ident=krw_gebied_id)
    except Area.DoesNotExist:
        pass

    report_bloks = []

    report_bloks.append({
        'title': 'Algemeen',
        'algemeen': True,
        'report_templates': ReportTemplate.objects.filter(kind='algemeen'),
        'generated_reports': GeneratedReport.objects.filter(template__kind='algemeen'),
    })

    report_bloks.append({
        'title': 'KRW waterlichaam',
        'algemeen': False,
        'selection_id': 'select_krw_waterlichaam',
        'area': krw_gebied,
        'report_templates': ReportTemplate.objects.filter(kind='krw'),
        'generated_reports': GeneratedReport.objects.filter(template__kind='krw', area = krw_gebied)
    })

    report_bloks.append({
        'title': 'Aan/afvoergebieden',
        'algemeen': False,
        'selection_id': 'select_aan_afvoergebied',
        'area': aan_afvoergebied,
        'report_templates': ReportTemplate.objects.filter(kind='aan_afvoer'),
        'generated_reports': GeneratedReport.objects.filter(template__kind='aan_afvoer', area = aan_afvoergebied)
    })

    report_templates = {}


    return render_to_response(
        template,
        {
            'data_sets': data_sets,
            'report_bloks': report_bloks,

        },
        context_instance=RequestContext(request))



class Error(Exception):
    """Base class for errors in this module."""
    pass

class OutOfRangeError(Error):
    def __init__(self, msg):
        Exception.__init__(self, msg)




def get_pdf_report(report_template, username, area_id=None):

    report_module = __import__(report_template.generation_module, fromlist='something')

    report = getattr(report_module, report_template.generation_function)(username, format='html', area_id=area_id)

    print "report: ", report
    
    # template = get_template(report_module)
    # context = Context(context_dict)
    # html = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(
    StringIO.StringIO(report.encode("ISO-8859-1")), result) # Latin
    # StringIO.StringIO(html.encode("UTF-8")), result) # Unicode
    if not pdf.err:
        return result
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))


from django.utils import encoding

def convert_unicode_to_string(x):
    """
    >>> convert_unicode_to_string(u'ni\xf1era')
    'niera'
    """
    return encoding.smart_str(x, encoding='ascii', errors='ignore')

def stringify(value):

    try:
        if type(value) == unicode:
            return convert_unicode_to_string(value)
        else:
            return value
    except Exception, e:
        return 'field error: %s'%e


def create_csv_from_grid(grid):
    """
        create csv from a grid with rows and cols
    """

    buffer = StringIO.StringIO()

    print len(grid)

    grid = [[stringify(value) for value in row] for row in grid]

    print len(grid)

    csv_writer = csv.writer(buffer, delimiter=',',
                            quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerows(grid)
    buffer.seek(0)
    return buffer

def create_xls_from_grid(grid):
    """
        create csv from a grid with rows and cols
    """


    wb = excel.Workbook()
    ws = wb.add_sheet('rapport')

    font1 = excel.Formatting.Font()
    font1.name = 'Arial'
    font1.height = 200
    font1.bold = True

    font2 = excel.Formatting.Font()
    font2.name = 'Arial'
    font2.height = 160

    borders = excel.Borders()
    borders.bottom = 10

    st1 = excel.XFStyle()
    st2 = excel.XFStyle()

    st1.font = font1
    st2.font = font2
    st1.borders = borders

    wb.add_style(st1)
    wb.add_style(st2)

    c = 0
    r = 0

    for row in grid:
        c = 0
        for value in row:
            if value != None:
                try:
                    ws.write( r, c, stringify(value))
                except UnicodeEncodeError, e:
                    ws.write( r, c, 'field error: %s'%e)
            c = c + 1
        if c%40 == 0:
            ws.flush_row_data()
        r = r + 1

    buffer = StringIO.StringIO()
    wb.save(buffer)
    del wb
    buffer.seek(0)

    return  buffer

def generate_report(request_or_username, format='pdf', report_id=None, area_id=None, return_as_file=False):
    '''
        function calls generation functions (specified in the configuration) and returns document
    '''

    if type(request_or_username) == str:
        username = request_or_username
    else:
        username = request_or_username.user.get_full_name()



    report_template = ReportTemplate.objects.get(pk=report_id)
    report_module = __import__(report_template.generation_module, fromlist='something')
    #todo, improve interaction with return, saving achieve, etc

    if format == 'pdf':
        pdf = get_pdf_report(report_template, username, area_id)
        if return_as_file:
            return pdf
        else:
            return HttpResponse(pdf.getvalue(), mimetype='application/pdf')

    elif format == 'html':
        report = getattr(report_module, report_template.generation_function)(username, format='html', report_id=report_id, area_id=area_id)
        return HttpResponse(report, mimetype='text/html')

    elif format == 'rtf':
        report = getattr(report_module, report_template.generation_function)(username, format='rtf', report_id=report_id, area_id=area_id)
        if return_as_file:
            return report
        else:
            return HttpResponse(report, mimetype='application/rtf')

    elif format == 'csv':
        grid = getattr(report_module, report_template.generation_function)(username, format='grid', report_id=report_id, area_id=area_id)
        csv = create_csv_from_grid(grid)
        if return_as_file:
            return csv
        else:
            response = HttpResponse(csv.read(), mimetype='application/csv')
            response['Content-Disposition'] = 'attachment; filename="%s.csv"'%'rapport'
            return response

    elif format == 'xls':
        grid = getattr(report_module, report_template.generation_function)(username, format='grid', report_id=report_id, area_id=area_id)
        xls = create_xls_from_grid(grid)
        if return_as_file:
            return xls
        else:
            response = HttpResponse(xls.read(), mimetype='application/xls')
            response['Content-Disposition'] = 'attachment; filename="%s.xls"'%'rapport'
            return response
    else:
        return HttpResponse('format niet ondersteund', mimetype='text/html')


def get_generated_report(request,generated_report_id=None,file_format='pdf'):

    generated_report = get_object_or_404(GeneratedReport, id=generated_report_id)
    response = HttpResponse(generated_report.get_file(file_format), mimetype='application/'+file_format)
    response['Content-Disposition'] = 'attachment;'
    return response
