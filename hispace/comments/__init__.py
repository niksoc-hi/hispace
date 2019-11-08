def get_model():
    """gets custom comment model. see https://django-contrib-comments.readthedocs.io/en/latest/custom.html"""
    from hispace.comments.models import MyComment

    return MyComment
