# djgo

## Description

This package provides some shortcuts for your django app.

## Installation

    pip install djgo

- [PyPI page](https://pypi.org/project/djgo/)
- [GitHub page](https://github.com/Ceterai/djgo/)

## Usage

djgo has shortcuts for different parts of the app.
To use it, simply import it with `import djgo`.

### manage.py

Method `start_django()` (or `manage()`) is a shortcut for launching Django.

### wsgi.py

Method `set_wsgi()` is a shortcut that sets Django settings env variable and returns default wsgi application.

### urls.py

Method `load_app()` is a shortcut that loads and returns an app module or its part.

### app/contrib.py

Method `app_config()` is a shortcut that sets Django app config. Example:

    from djpp import app_config
    default_app_config = app_config(verbose_name='My Cool App')

### app/models.py

Decorator `@meta` is a shortcut that sets meta and \_\_str\_\_() for your model.  
WARNING: All meta defined this way won't register in migrations.  
Example:

    @meta(single='My Client', plural='My Clients', display='name')
    class Client(models.Model):
        name = models.CharField()

is equal to

    class Client(models.Model):
        name = models.CharField()
        class Meta:
            verbose_name = 'My Client'
            verbose_name_plural = 'My Clients'
        def \_\_str\_\_():
            return self.name

except the meta (name and verbose_name) won't register in migrations.

You can also pass functions to `display`:

    @meta('My Client', display=lambda self: 'Cool ' + str(self.name))
    class Client(models.Model):
        name = models.CharField()

is equal to

    class Client(models.Model):
        name = models.CharField()
        class Meta:
            name = 'My Client'
            verbose_name = 'My Client'
        def \_\_str\_\_():
            return 'Cool ' + str(self.name)

except the meta (name and verbose_name) won't register in migrations.

### djgo.admin

djgo has a small set of methods for admin site and admin.py file:

- `admin.urls` is a shortcut for `path('url', admin.site.urls)`, except adds '/' in the end of your url string if it doesn't have one.
- `admin.meta` is a shortcut for setting `admin.site.site_header` and `admin.site.site_title`.
- `admin.clear_models` is a shortcut for clearing models from admin site registry.
- `admin.quick_inline` is a **decorator** for setting some tabular inline params.

### Other features

You can also access settings through djgo with `djgo.settings`!

Lastly, djgo provides a small `log()` method for printing some info.
