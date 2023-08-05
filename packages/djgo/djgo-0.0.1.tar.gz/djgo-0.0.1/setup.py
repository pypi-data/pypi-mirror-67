# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['djgo']

package_data = \
{'': ['*']}

install_requires = \
['django>=3.0.5,<4.0.0']

setup_kwargs = {
    'name': 'djgo',
    'version': '0.0.1',
    'description': 'A pack of shortcuts for Django.',
    'long_description': "# djgo\n\n## Description\n\nThis package provides some shortcuts for your django app.\n\n## Installation\n\n    pip install djgo\n\n- [PyPI page](https://pypi.org/project/djgo/)\n- [GitHub page](https://github.com/Ceterai/djgo/)\n\n## Usage\n\ndjgo has shortcuts for different parts of the app.\nTo use it, simply import it with `import djgo`.\n\n### manage.py\n\nMethod `start_django()` (or `manage()`) is a shortcut for launching Django.\n\n### wsgi.py\n\nMethod `set_wsgi()` is a shortcut that sets Django settings env variable and returns default wsgi application.\n\n### app/contrib.py\n\nMethod `app_config()` is a shortcut that sets Django app config. Example:\n\n    from djpp import app_config\n    default_app_config = app_config(verbose_name='My Cool App')\n\n### app/models.py\n\nDecorator `@meta` is a shortcut that sets meta and \\_\\_str\\_\\_() for your model.  \nWARNING: All meta defined this way won't register in migrations.  \nExample:\n\n    @meta(single='My Client', plural='My Clients', display='name')\n    class Client(models.Model):\n        name = models.CharField()\n\nis equal to\n\n    class Client(models.Model):\n        name = models.CharField()\n        class Meta:\n            verbose_name = 'My Client'\n            verbose_name_plural = 'My Clients'\n        def \\_\\_str\\_\\_():\n            return self.name\n\nexcept the meta (name and verbose_name) won't register in migrations.\n\nYou can also pass functions to `display`:\n\n    @meta('My Client', display=lambda self: 'Cool ' + str(self.name))\n    class Client(models.Model):\n        name = models.CharField()\n\nis equal to\n\n    class Client(models.Model):\n        name = models.CharField()\n        class Meta:\n            name = 'My Client'\n            verbose_name = 'My Client'\n        def \\_\\_str\\_\\_():\n            return 'Cool ' + str(self.name)\n\nexcept the meta (name and verbose_name) won't register in migrations.\n\n### djgo.admin\n\ndjgo has a small set of methods for admin site and admin.py file:\n\n- `admin.urls` is a shortcut for `path('url', admin.site.urls)`, except adds '/' in the end of your url string if it doesn't have one.\n- `admin.meta` is a shortcut for setting `admin.site.site_header` and `admin.site.site_title`.\n- `admin.clear_models` is a shortcut for clearing models from admin site registry.\n- `admin.quick_inline` is a **decorator** for setting some tabular inline params.\n\n### Other features\n\nYou can also access settings through djgo with `djgo.settings`!\n\nLastly, djgo provides a small `log()` method for printing some info.\n",
    'author': 'Ceterai',
    'author_email': 'ceterai@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Ceterai/djgo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
