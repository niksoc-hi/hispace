from django_comments.abstracts import CommentAbstractModel
from model_utils.models import TimeStampedModel
from vote.models import VoteModel


# TODO: `Comment` model name clashes with django_comment's model, though we aren't using that model
# This forces us to use this ugly name
class MyComment(CommentAbstractModel, VoteModel, TimeStampedModel):
    """ Comment Model. Don't access directly, use comments.get_model() """
