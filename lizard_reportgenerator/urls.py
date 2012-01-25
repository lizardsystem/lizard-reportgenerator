# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin

from lizard_ui.urls import debugmode_urlpatterns

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', index, name='htmlrapportage-index'),
    url(r'^generate/rtf/$', generate_rtf, name='htmlrapportage-generate-rtf'),
    url(r'^generate/pdf/$', generate_pdf, name='htmlrapportage-generate-pdf'),
    )
urlpatterns += debugmode_urlpatterns()
