import os

from django.contrib.staticfiles import finders
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError


def get_filename_by(obj_str, path_dir=None):
    """Example: get_filenames_by('github') -> 'dir/git.png'"""

    if not path_dir:
        path_dir = finders.find("images/logos/")
    for f in os.listdir(path_dir):
        if f.split(".")[0] in obj_str:
            return f


def get_path_by(obj_str, path_dir=None):
    fn = get_filename_by(obj_str, path_dir)
    if not fn:
        return
    return finders.find(f"images/logos/{fn}")


def validate_avatar(image):
    sizes = [(400, 400), (500, 500)]
    size = get_image_dimensions(image)

    if size not in sizes:
        text = "Image size can be: "
        for w, h in sizes:
            text = f"{text}{w}x{h}px "

        raise ValidationError(text)
