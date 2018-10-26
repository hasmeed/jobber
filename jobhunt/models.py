from django.db import models
from django.contrib.auth.models import AbstractUser


# class Identity(AbstractUser):
#     is_provider = models.BooleanField(default=False)
#     is_seeker = models.BooleanField(default=False)


# class CommonInfo(models.Model):
#     IsActive = models.BooleanField(default=True)
#     IsDeleted = models.BooleanField(default=False)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True


# class CommonAccountInfo(CommonInfo):
#     firstname = models.CharField(max_length=50, null=True, blank=True)
#     lastname = models.CharField(max_length=50, null=True, blank=True)
#     email = models.CharField(max_length=50, null=True, blank=True)
#     phonenumber = models.CharField(max_length=120, null=True, blank=True)
#     address = models.CharField(max_length=120, null=True, blank=True)
#     landline = models.CharField(max_length=120, null=True, blank=True)
#     skype = models.CharField(max_length=120, null=True, blank=True)
#     website = models.CharField(max_length=120, null=True, blank=True)

#     class Meta:
#         abstract = True


class Seeker(models.Model):
    # identity = models.OneToOneField(Identity, on_delete=models.CASCADE)
    salary = models.CharField(max_length=120, null=True, blank=True)
    location = models.CharField(max_length=120, null=True, blank=True)
    headline = models.CharField(max_length=120, null=True, blank=True)
    age = models.CharField(max_length=120, null=True, blank=True)
    # tags = models.CharField(max_length = 120, null=True, blank=True)

    # social media
    facebook = models.CharField(max_length=120, null=True, blank=True)
    google = models.CharField(max_length=120, null=True, blank=True)
    pintrest = models.CharField(max_length=120, null=True, blank=True)
    twitter = models.CharField(max_length=120, null=True, blank=True)
    git = models.CharField(max_length=120, null=True, blank=True)
    instagram = models.CharField(max_length=120, null=True, blank=True)
    youtube = models.CharField(max_length=120, null=True, blank=True)
    dribbble = models.CharField(max_length=120, null=True, blank=True)
    # end of social media
