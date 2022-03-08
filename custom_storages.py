from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """ custom static file storage """
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    """ custom media file storage """
    location = settings.MEDIAFILES_LOCATION