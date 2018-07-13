from django.templatetags.static import *


class CustomStaticNode(StaticNode):

    def url(self, context):
        path = self.path.resolve(context)
        domain = context.get('request').META.get('HTTP_HOST')
        return self.handle_simple(path, domain)

    @classmethod
    def handle_simple(cls, path, domain):
        if apps.is_installed('django.contrib.staticfiles'):
            from django.contrib.staticfiles.storage import staticfiles_storage
            return staticfiles_storage.url(path, domain=domain)
        else:
            return urljoin(PrefixNode.handle_simple("STATIC_URL"), quote(path))


@register.tag('static')
def do_static(parser, token):
    """
    Join the given path with the STATIC_URL setting.

    Usage::

        {% static path [as varname] %}

    Examples::

        {% static "myapp/css/base.css" %}
        {% static variable_with_path %}
        {% static "myapp/css/base.css" as admin_base_css %}
        {% static variable_with_path as varname %}
    """
    return CustomStaticNode.handle_token(parser, token)


def static(path):
    """
    Given a relative path to a static asset, return the absolute path to the
    asset.
    """
    return CustomStaticNode.handle_simple(path)
