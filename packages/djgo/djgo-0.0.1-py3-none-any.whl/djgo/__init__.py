from .djgo import manage, meta, app_config, set_wsgi, log, load_module
from . import admin
from django.conf import settings


def start_django(settings_module, name=None, sys_argv=None, error_msg=None):
    """Same as djgo.manage(). Invokes usual manage.py activity.\n
    Params:
    - settings_module - relative path to settings file, separated with dots.
    - name (optional) - the __name__ attribute of manage.py. If provided,
    will perform 'if __name__ == '__main__'' check.
    - sys_argv (optional) - if provided, will be used instead of sys.argv.
    """
    manage(settings_module, name, sys_argv, error_msg)
