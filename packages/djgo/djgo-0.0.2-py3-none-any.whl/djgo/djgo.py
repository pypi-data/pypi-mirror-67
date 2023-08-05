import os
import sys


def manage(settings_module, name=None, sys_argv=None, error_msg=None):
    """Invokes usual manage.py activity - launches django.\n
    Params:
    - settings_module - relative path to settings file, separated with dots.
    - name (optional) - the __name__ attribute of manage.py. If provided,
    will perform 'if __name__ == '__main__'' check.
    - sys_argv (optional) - if provided, will be used instead of sys.argv.
    """
    if name == '__main__' or not name:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
                error_msg or
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            ) from exc
        execute_from_command_line(sys_argv if sys_argv else sys.argv)


def meta(single=None, plural=None, display=None):
    """A compact way to set verbose name and the __str__ method in a model.\n
    WARNING! All meta defined this way won't register in migrations.\n
    Params:
    - single - if provided, sets verbose_name of the model.
    - plural - if provided, sets verbose_name_plural of the model.
    - display - if provided as a string, will be used as an attribute name
    to return with __str__.

    Example:

        @meta(display='name')
        class MyModel:
            name = CharField()

    translates to

        class MyModel:
            name = CharField()
            def __str__(self):
                return self.name

    You can also pass your own functions to display, in this case they will
    be set as __str__. Don't forget to pass `self` to your function first!
    """
    def decorator(Model):
        if single:
            Model._meta.verbose_name = single
        if single or plural:
            Model._meta.verbose_name_plural = plural if plural else single
        if type(display) == str:
            Model.__str__ = lambda self: self.__dict__[display]
        elif display:
            Model.__str__ = display
        return Model
    return decorator


def app_config(verbose_name=None, appname=None):
    """A compact way to set contrib for your app.\n
    Params:
    - verbose_name - if provided, sets verbose_name of the app. Otherwise,
    the normal name is used.
    - appname - if provided, sets an explicit name for the app. Otherwise,
    the folder name is used.

    Return value is a string that you should set your `default_app_config` to.
    """
    from django.apps import AppConfig
    import inspect
    vn = verbose_name
    f = inspect.getouterframes(inspect.currentframe(), 2)[1].filename
    path = os.path.basename(os.path.dirname(f))
    class AppConfig(AppConfig):
        name = appname or path
        verbose_name = vn or name
    setattr(sys.modules[path], 'AppConfig', AppConfig)
    return path + '.AppConfig'


def set_wsgi(settings_module=None, wsgi_module=None, name=None):
    """A compact way to set your wsgi.\n
    Params:
    - settings_module - if provided, performs
    `os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)`.
    - wsgi_module and name - if both are provided, performs a
    `name == wsgi_module` check before returning wsgi application.
    Name is supposed to be your file's __name__ in this situation.

    Return value is get_wsgi_application().
    """
    from django.core.wsgi import get_wsgi_application
    if settings_module:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
    if name == wsgi_module or not wsgi_module:
        return get_wsgi_application()


def log(settings, name_var=None, env_var=None, key_msg=False, prt_msg=True):
    """A short method for printing out some useful info.\n
    Params:
    - settings - your settings module.
    - name_var (str) - if provided, prints value of setting with this name.
    - env_var (str) - if provided, will print out stage info from setting
    with this name. If stage is `None`, will print `Debug`.
    - prt_msg - if `True`, prints and returns the output, else
    just returns it.
    """
    out = []
    if name_var:
        out.append(getattr(settings, name_var))
    if env_var:
        stage = (getattr(settings, env_var) or 'debug').upper()
        out.append(stage + ' stage.')
    if key_msg and os.getenv('SECRET_KEY'):
        out.append('\nFound a secret key!')
    msg = ' '.join(out)
    if prt_msg:
        print(msg)
    return msg


def load_app(module_name, objects=None):
    """Simply loads and returns an app module for you.\n
    Params:
    - module_name - module name of your app.
    - objects (str) - if provided, returns a certain part of the module
    instead of the whole thing. Example:
    `load_app('my_app', objects='views')` will return `my_app.views`.
    """
    from importlib import import_module
    if objects:
        return import_module(module_name + '.' + objects)
    else:
        return import_module(module_name)
