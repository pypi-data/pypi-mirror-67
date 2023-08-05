import os
import environ

from django.conf import settings

# initialize django-environ
env = getattr(settings, 'env', environ.Env())

APP_NAME = getattr(settings, 'APP_NAME', env('APP_NAME', default='django_project'))
ROOT_DIR = getattr(settings, 'ROOT_DIR', environ.Path(__file__))

BACKUP_FILE_PREFIX = 'backup'
DJANGO_PROJECT_BACKUP_DUMPDATA_JSON_FILENAME = 'dump_all.json'

_DUMPDATA_EXCLUDED_MODELS = [
                    'auth.permission',
                    'contenttypes',
                    'sessions',
                    'admin',
                 ]

if 'django_sso_app' in settings.INSTALLED_APPS:
    _DUMPDATA_EXCLUDED_MODELS += [
        'django_sso_app.passepartout',
        'django_sso_app.device'
    ]


_PUBLIC_ASSETS_FOLDERS = [
    settings.PUBLIC_ROOT,
]

_PRIVATE_ASSETS_FOLDERS = [
    settings.PRIVATE_ROOT,
]


DJANGO_PROJECT_BACKUP_DUMPDATA_EXCLUDED_MODELS = getattr(settings, 'DJANGO_PROJECT_BACKUP_DUMPDATA_EXCLUDED_MODELS',
                                                         env.list('DJANGO_PROJECT_BACKUP_DUMPDATA_EXCLUDED_MODELS',
                                                                  default=_DUMPDATA_EXCLUDED_MODELS))

DJANGO_PROJECT_BACKUP_PUBLIC_ASSETS_FOLDERS = getattr(settings, 'DJANGO_PROJECT_BACKUP_PUBLIC_ASSETS_FOLDERS',
                                               env.list('DJANGO_PROJECT_BACKUP_PUBLIC_ASSETS_FOLDERS',
                                                        default=_PUBLIC_ASSETS_FOLDERS))

DJANGO_PROJECT_BACKUP_PRIVATE_ASSETS_FOLDERS = getattr(settings, 'DJANGO_PROJECT_BACKUP_PRIVATE_ASSETS_FOLDERS',
                                               env.list('DJANGO_PROJECT_BACKUP_PRIVATE_ASSETS_FOLDERS',
                                                        default=_PRIVATE_ASSETS_FOLDERS))

_BACKUP_DESTINATION_FOLDER = os.path.abspath(os.path.join(ROOT_DIR, 'backups'))

DJANGO_PROJECT_BACKUP_DESTINATION_FOLDER = getattr(settings, 'DJANGO_PROJECT_BACKUP_DESTINATION_FOLDER',
                                                   env('DJANGO_PROJECT_BACKUP_DESTINATION_FOLDER',
                                                       default=_BACKUP_DESTINATION_FOLDER))
