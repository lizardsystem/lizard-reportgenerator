#!/usr/bin/python
# -*- coding: utf-8 -*-

# pylint: disable=C0111

# Copyright (c) 2012 Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.

import logging

from celery.task import task

import datetime

from lizard_reportgenerator.views import generate_report
from lizard_reportgenerator.models import ReportTemplate, GeneratedReport
from lizard_security.models import DataSet
from lizard_area.models import Area

from lizard_task.task import task_logging


@task()
@task_logging
def generate_reports(report_template_id=None,
               data_set=None,
               taskname="",
               username=None,
               levelno=20):
    """Import a waterbalance configuration from dbf.

    This function is provided for convenience only. It allows us to test the
    waterbalance configuration import without the need of a
    ConfigurationToValidate.

    """

    logger = logging.getLogger(taskname)

    report_template = ReportTemplate.objects.get(pk=report_template_id)
    formats = []
    if report_template.pdf_support:
        formats.append('pdf')
    if report_template.csv_support:
        formats.append('csv')
    if report_template.xls_support:
        formats.append('xls')
    #if report_templatet.rtf_support:
    #    pass

    if report_template.kind == 'algemeen':
        generated_report = GeneratedReport(
            template=report_template,
            area=None,
            data_set=DataSet.objects.get(pk=data_set) if data_set is not None else None,
            generated_on=datetime.datetime.now(),
        )
        #get id
        generated_report.save()
        for format in formats:
            file_io = generate_report(
                "automatische taak", format, report_template_id, data_set, True)
            generated_report.save_file(file_io, format, '%s_%s' % (
                    report_template.name, datetime.datetime.now().strftime('%d-%M-%Y_%Hu%M')))

        generated_report.save()

    else:
        print report_template.kind
        print '----'
        if report_template.kind == 'krw':
            area_class = Area.AREA_CLASS_KRW_WATERLICHAAM
        elif report_template.kind == 'aan_afvoer':
            area_class = Area.AREA_CLASS_AAN_AFVOERGEBIED

        data_set = DataSet.objects.get(pk=data_set)
        for area in Area.objects.filter(data_set=data_set, is_active=True, area_class=area_class):
            logger.info('report for area %s' % area.name)

            generated_report = GeneratedReport(
                template=report_template,
                area=area,
                data_set=data_set,
                generated_on=datetime.datetime.now(),
                )
            #get id
            generated_report.save()
            for format in formats:
                file_io = generate_report(
                    "automatische taak", format, report_template_id, area.ident, True)
                generated_report.save_file(file_io, format, '%s_%s_%s' % (
                        report_template.name.replace('/', '_'),
                        area.ident,
                        datetime.datetime.now().strftime('%d-%M-%Y_%Hu%M')))

            generated_report.save()
