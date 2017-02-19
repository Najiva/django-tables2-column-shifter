#!/usr/bin/env python
# encoding:utf-8
import os
import sys
import warnings

import django
from django.conf import settings
from django.test.utils import get_runner

if __name__ == "__main__":
    '''
    Testy projektu, przechodzimy po katalogu 'moduly' i dla
    każdego modułu wykonujemy testy zamieszczone w katalogu 'testy'
    '''
    warnings.simplefilter('always', DeprecationWarning)

    app_dir = os.path.join(os.path.dirname(__file__), 'django_tables2_column_shifter')
    sys.path.insert(0, app_dir)

    # configure
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=2)
    failures = test_runner.run_tests(['tests'])
    sys.exit(bool(failures))
