from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'mobile_api.tests.test_context_processor')

from lms.djangoapps.mobile_api.tests.test_context_processor import *
