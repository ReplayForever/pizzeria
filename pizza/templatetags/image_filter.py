from django.template.library import Library


register = Library()


@register.filter
def is_exists(image):
    try:
        image.file
    except FileNotFoundError:
        return False

    return True
