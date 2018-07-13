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
            pieces = domain.split('.')
            subdomain = pieces[0]
            if subdomain.isalpha():
                subdomain_name = os.path.join(subdomain, name)
                result = super().url(subdomain_name, parameters, expire)
                print('first result: ' + result)

        if not result:
            result = super().url(name, parameters, expire)
            print('second result: ' + result)

        return result
