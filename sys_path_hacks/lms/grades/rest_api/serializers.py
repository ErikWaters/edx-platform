from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'grades.rest_api.serializers')

from lms.djangoapps.grades.rest_api.serializers import *
