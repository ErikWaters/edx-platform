from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'lti_provider.tests.test_signature_validator')

from lms.djangoapps.lti_provider.tests.test_signature_validator import *
