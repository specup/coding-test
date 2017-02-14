from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Content(models.Model):
    subject = models.CharField(max_length=100)
    price = models.IntegerField()


class UserContentManager(models.Manager):
    @staticmethod
    def create_usercontent(user_id, content_id):
        user = User.objects.get(id=user_id)
        content = Content.objects.get(id=content_id)
        return UserContent.objects.create(
            user=user,
            content=content
        )


class UserContent(models.Model):
    user = models.ForeignKey(User)
    content = models.ForeignKey(Content)

    objects = UserContentManager()


class Payment(models.Model):
    amount = models.IntegerField()
    user_content = models.ForeignKey(UserContent)
