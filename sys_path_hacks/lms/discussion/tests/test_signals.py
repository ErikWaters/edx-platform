from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'discussion.tests.test_signals')

from lms.djangoapps.discussion.tests.test_signals import *
