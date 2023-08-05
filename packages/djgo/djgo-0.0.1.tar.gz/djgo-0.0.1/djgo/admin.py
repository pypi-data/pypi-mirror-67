from django.contrib import admin


def quick_inline(model, verbose_name=None, fields=None, readonly_fields=None,
                can_delete=None, max_num=None, extra=None):
    """A shortcut for setting some tabular inline params.
    All except `model` are optional.
    """
    def decorator(Inline):
        Inline.model = model
        if fields:
            Inline.fields = fields
        if readonly_fields:
            Inline.readonly_fields = readonly_fields
        if verbose_name:
            Inline.verbose_name = verbose_name
        if can_delete:
            Inline.can_delete = can_delete
        if max_num:
            Inline.max_num = max_num
        if extra:
            Inline.extra = extra
        return Inline
    return decorator


def clear_models(*models, groups=False, users=False):
    """A shortcut for clearing models from admin site registry.\n
    Params:
    - models (iterable) - if provided, unregisters these models.
    - groups - if `True`, unregisters Group from `django.contrib.auth.models`.
    - users - if `True`, unregisters User from `django.contrib.auth.models`.
    """
    from django.contrib.auth.models import Group, User
    if users:
        admin.site.unregister(User)
    if groups:
        admin.site.unregister(Group)
    if models:
        for model in models:
            admin.site.unregister(model)


def urls(url='admin/'):
    """A shortcut for `path(url, admin.site.urls)`.
    """
    from django.urls import path
    if url[-1] != '/':
        url = url + '/'
    return path(url, admin.site.urls)


def meta(header=None, title=None):
    """A shortcut for setting `admin.site.site_header`
    and `admin.site.site_title`.
    """
    if header:
        admin.site.site_header = header
    if title:
        admin.site.site_title = title
