# -*- coding: utf-8 -*-
import os

from setuptools import setup
from setuptools import find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as f:
    VERSION = f.read().strip()

tests_require = ['django-storages', 'model-bakery',
                 'faker', 'django_environ']

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='inte-edc',
    version=VERSION,
    author=u'Erik van Widenfelt',
    author_email='ew2789@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/inte-africa-trial/inte-edc',
    license='GPL license, see LICENSE',
    description='META Trial EDC (http://www.isrctn.com/ISRCTN76157257)',
    long_description=README,
    zip_safe=False,
    keywords='django inte africa EDC',
    install_requires=[
        'boto3',
        'bs4',
        'celery',
        'django==2.2.9',
        'django-celery-beat',
        'django-celery-results',
        'django-collect-offline',
        'django-collect-offline-files',
        'django-environ',
        'django-redis',
        'django-storages',
        'edc-action-item',
        'edc_adverse_event',
        'edc-appointment',
        'edc-consent',
        'edc-constants',
        'edc-form-describer',
        'edc-form-label',
        'edc-form-validators',
        'edc-lab',
        'edc_lab_dashboard',
        'edc-list-data',
        'edc-metadata',
        'edc-metadata-rules',
        'edc-offstudy',
        'edc_pharmacy',
        'edc-reportable',
        'edc_review_dashboard',
        'edc-sites',
        'edc-subject-dashboard',
        'edc_constants',
        'edc_export',
        'edc_model_admin',
        'edc_notification',
        'edc_pdutils',
        'edc_reference',
        'edc_reports',
        'edc_screening',
        'edc_visit_schedule',
        'gunicorn',
        'python-memcached',
        'pytz',
        'sentry_sdk',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    python_requires=">=3.7",
    tests_require=tests_require,
    test_suite='runtests.main',
)
