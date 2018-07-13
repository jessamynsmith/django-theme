import os
from django.conf import settings as django_settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = django_settings.STATICFILES_LOCATION

    def __init__(self, acl=None, bucket=None, **settings):
        super().__init__(acl, bucket, **settings)

    def url(self, name, domain=None, parameters=None, expire=None):
        result = None
        if domain:
            domain_no_port = domain.split(':')[0]
            pieces = domain_no_port.split('.')
            subdomain = pieces[0]
            name_with_domain = os.path.join(subdomain, name)
            if self.exists(name_with_domain):
                result = super().url(name_with_domain, parameters, expire)

        if not result:
            result = super().url(name, parameters, expire)

        return result
