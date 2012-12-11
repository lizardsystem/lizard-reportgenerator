from setuptools import setup

version = '0.7.2.dev0'

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('TODO.rst').read(),
    open('CREDITS.rst').read(),
    open('CHANGES.rst').read(),
    ])

install_requires = [
    'Django',
    'django-extensions',
    'django-nose',
    'lizard-ui >= 3.0',
    'lizard-area',
    'pkginfo',
    'clint',
    'PyRTF',
    'xlwt',
    'reportlab',
    #'pisa',
    'html5lib',
    'pyPdf',
    ],

tests_require = [
    ]

setup(name='lizard-reportgenerator',
      version=version,
      description="Generates reports from data sources (not automatically, needs to be coded) and generated PDF and RTF documents",
      long_description=long_description,
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Programming Language :: Python',
                   'Framework :: Django',
                   ],
      keywords=[],
      author='Gijs Nijholt',
      author_email='gijs.nijholtnelen-schuurmans.nl',
      url='',
      license='GPL',
      packages=['lizard_reportgenerator'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require = {'test': tests_require},
      entry_points={
          'console_scripts': [
          ]},
      )
