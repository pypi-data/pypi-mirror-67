import importlib

from .conf import HOOK_SETTINGS
from django.conf import settings
from .old_conf import config as global_config


def get_scheme(request, config=None):
    if config is None:
        config = global_config

    scheme = "https"
    if settings.DEBUG and request is not None:
        if "HTTP_X_FORWARDED_PROTO" in request.META:
            scheme = request.META["HTTP_X_FORWARDED_PROTO"]
        else:
            scheme = request.scheme
    return scheme


def get_hook(name, config):
    if name in HOOK_SETTINGS:
        hook_setting = getattr(config, name)
        if hook_setting != "":
            module_path, function_name = hook_setting.rsplit(".", 1)
            module = importlib.import_module(module_path)
            function = getattr(module, function_name)

            return function
    return None
