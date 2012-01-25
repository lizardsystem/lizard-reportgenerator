# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.conf import settings
from lizard_htmlreport.models import ReportTemplate
from lizard_htmlreport.models import GeneratedReport
from lizard_security.models import DataSet

from PyRTF import *
import os
from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponse
from django.template import Context
from django.template import RequestContext



def OpenFile( name ) :
	return file( '%s.rtf' % name, 'w' )


def index(request, template='lizard_htmlreport/index.html'):

    kind = request.GET.get('kind')

    if kind == "krw":
        title = "KRW"
        reports = ReportTemplate.objects.filter(kind=kind)

    elif kind == "aan_afvoer":
        title = "Aan en afvoergebieden"
        reports = ReportTemplate.objects.filter(kind=kind)
        
    else:
        title = "Algemeen"
        reports = ReportTemplate.objects.filter(kind="algemeen")
        
    

    return render_to_response(
        template,
        locals(),
        context_instance=RequestContext(request))



def generate_rtf(request):
    name = request.GET.get('name')
    if name:
        
        # Generate RTF file
        doc = Document()
        ss = doc.StyleSheet
        section = Section()
        doc.Sections.append(section)

        section.append('Example 1')
        section.append('')

        section.append('Lorem ipsum dolor sit amet'
                        'consectetur adipisicing elit, '
                        'sed do eiusmod tempor incididunt'
                        'ut labore et dolore magna aliqua. '
                        'Ut enim ad minim veniam, quis'
                        'nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea'
                        'commodo consequat. Duis aute'
                        'irure dolor in reprehenderit in'
                        'voluptate velit esse cillum dolore'
                        'eu fugiat nulla pariatur.')

        DR = Renderer()
        DR.Write(doc, OpenFile(name))
        
        print OpenFile(name)
        print open(name+".rtf", "r")
        response = HttpResponse(
            open(name+".rtf", "r"),
            content_type='application/rtf'
        )
        response['Content-Disposition'] = 'attachment; filename=report' + str(name) + '.rtf'

        return HttpResponse(response)
    else:
        raise Http404



def generate_pdf(request):
    raise http404
