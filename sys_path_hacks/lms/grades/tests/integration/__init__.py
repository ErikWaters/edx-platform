from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'grades.tests.integration')

from lms.djangoapps.grades.tests.integration import *
