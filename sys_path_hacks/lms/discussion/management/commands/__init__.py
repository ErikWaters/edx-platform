from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'discussion.management.commands')

from lms.djangoapps.discussion.management.commands import *
