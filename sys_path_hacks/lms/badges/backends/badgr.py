from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'badges.backends.badgr')

from lms.djangoapps.badges.backends.badgr import *
