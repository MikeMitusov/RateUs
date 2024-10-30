import os

from django.contrib.staticfiles import finders


def get_filename_by(obj_str, path_dir=None):
    """Example: get_filenames_by('github') -> 'dir/git.png'"""

    if not path_dir:
        path_dir = finders.find("images/logos/")
    for f in os.listdir(path_dir):
        if f.split(".")[0] in obj_str:
            return f
