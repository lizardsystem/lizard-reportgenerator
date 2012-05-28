#!/usr/bin/python
# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

from django.core.management.base import BaseCommand
from lizard_reportgenerator.tasks import generate_reports

import logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Exports 'esf into dbf file.
    """

    help = ("Example: bin/django generate_report")

    def handle(self, *args, **options):
        self.generate_report()

    def generate_report(self):

        logger.info("start")
        generate_reports(3,2)
        logger.info("Finished.")
