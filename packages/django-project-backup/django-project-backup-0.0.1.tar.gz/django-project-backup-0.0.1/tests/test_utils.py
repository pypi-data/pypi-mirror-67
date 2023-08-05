# -*- coding: utf-8 -*-
import os

# import pytest
from django_project_backup.utils.common import get_backup_name_by_path

__author__ = "pai"
__copyright__ = "pai"
__license__ = "mit"


def test_get_backup_name():
    path = os.path.join('app', 'django_project', 'private')
    backup_name = get_backup_name_by_path(path)

    assert backup_name == 'private'
