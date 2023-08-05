import os


def get_backup_name_by_path(path):
    return str(path).split(os.sep)[-1:][0]
