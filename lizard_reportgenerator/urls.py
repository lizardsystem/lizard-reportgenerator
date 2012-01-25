# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin

from lizard_ui.urls import debugmode_urlpatterns

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', index, name='reportgenerator-index'),
    url(r'^generate/rtf/$', generate_rtf, name='reportgenerator-generate-rtf'),
    url(r'^generate/pdf/$', generate_pdf, name='reportgenerator-generate-pdf'),
    )
urlpatterns += debugmode_urlpatterns()
