Changelog of lizard-reportgenerator
===================================================


0.6.8 (unreleased)
------------------

- Fixed error in index.html template in case of supporting doc format. 


0.6.7 (2012-10-26)
------------------

- Implemented report generator for rtf, doc, docx file formats.

- Added doc_support to field to RepportTemplate model.

- Renamed varaibel 'format' to 'file_format'.


0.6.6 (2012-06-20)
------------------

- Make pdf generator try two types of encoding

- Monkeypatch urllib2 and httplib when retrieving images for the pdf.


0.6.5 (2012-06-15)
------------------

- Changed loging of celery task.

- Fixed pylint errors.


0.6.4 (2012-06-06)
------------------

- fixes for ie


0.6.3 (2012-06-01)
------------------

- open html-report in new window (pp 358)


0.6.2 (2012-05-30)
------------------

- removed duplicated report links (pp ??)


0.6.1 (2012-05-30)
------------------

- Fix ydev version problem.


0.6 (2012-05-29)
----------------

- bugfix in userrights

- small improvement in index page for unselected area


0.5 (2012-05-29)
----------------

- improved report overview page

- added download functionality for history

- pdf, csv and excel support


0.4 (2012-02-02)
----------------

- Nothing changed yet.


0.3 (2012-01-31)
----------------

- Nothing changed yet.


0.2 (2012-01-25)
----------------

- Nothing changed yet.


0.1 (2012-01-25)
----------------
- This project was copied from an earlier attempt, but wasn't named
  properly (lizard-htmlreport) and had buildout configuration trouble.

- Initial library skeleton created by nensskel.  [Gijs Nijholt]
