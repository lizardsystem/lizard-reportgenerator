# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin

from lizard_reportgenerator.views import index
from lizard_reportgenerator.views import generate_report

from lizard_ui.urls import debugmode_urlpatterns

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', index, name='reportgenerator-index'),
    url(r'^generate/(?P<format>.*)/(?P<report_id>.*)/(?P<area_id>.*)/$', generate_report, name='reportgenerator-generate'),
    )
urlpatterns += debugmode_urlpatterns()
