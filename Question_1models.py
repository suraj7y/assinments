from lib2to3.pgen2.tokenize import blank_re

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    city = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=10)
    image = models.imageField(upload_to='prof', blank=True)

    def __str__(self):
        return "%s" % self.user.username


class Post(models.Model):
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User)


class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, null=True)

    @classmethod
    def make_friends(cls, current_user, new_friend):
        friend, created = cls.object.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friends(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_created(
            current_user=current_user
        )
        friend.users.remove(new_friend)