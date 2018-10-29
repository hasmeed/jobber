from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from rest_framework.reverse import reverse as api_reverse



class Identity(AbstractUser):
    is_provider = models.BooleanField(default=False)
    is_seeker = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)


class CommonInfo(models.Model):
    IsActive = models.BooleanField(default=True)
    IsDeleted = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        abstract = True


class CommonAccountInfo(CommonInfo):
    firstname = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    phonenumber = models.CharField(max_length=120, null=True, blank=True)
    address = models.CharField(max_length=120, null=True, blank=True)
    landline = models.CharField(max_length=120, null=True, blank=True)
    skype = models.CharField(max_length=120, null=True, blank=True)
    website = models.CharField(max_length=120, null=True, blank=True)

    class Meta:
        abstract = True


class Seeker(CommonInfo):
    identity = models.OneToOneField(Identity, on_delete=models.CASCADE, default='2')
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

    #end of social media


class Category(CommonInfo):
    name = models.CharField(max_length=120)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('slug', 'parent',)    #enforcing that there can not be two
        verbose_name_plural = "categories"       #categories under a parent with same 
                                                 #slug 
    # @property
    # def owner(self):
    #     return self.identity

    @property
    def title(self):
        return self.name 

    def __str__(self):                          
        full_path = [self.name]                  
                                                 
        k = self.parent                          

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])

    def get_services_uri(self,request=None):
        return api_reverse('api:categoryServices', kwargs={'category_slug':self.slug}, request=request)

def klass_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(klass_pre_save_reciever, Category)



class Service(CommonInfo):
    title = models.CharField(max_length=120)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    price = models.CharField(max_length=120, null=True, blank=True,)
    approximate_time = models.CharField(max_length=120)
    inclusions = models.TextField(help_text='enter each inclusion here sepereted with comma')
    exclusions = models.TextField(help_text='enter each inclusion here sepereted with comma')
    procedure = models.TextField(help_text='enter procedure to carry out the service')

    def get_cat(self):
        return self.category.slug

    def get_cat_list(self):           
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent

        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]

    def get_service_inclusions(self):
        return self.inclusions.split(',')

    def get_service_exclusions(self):
        return self.exclusions.split(',')

pre_save.connect(klass_pre_save_reciever, Service)

class Job(CommonInfo):
    job = models.ForeignKey(Service, on_delete=models.CASCADE)
    


# class Education(CommonInfo):
#     # education
#     degree = models.CharField(max_length=120, null=True, blank=True)
#     major = models.CharField(max_length=120, null=True, blank=True)
#     school = models.CharField(max_length=120, null=True, blank=True)
#     datefrom = models.CharField(max_length=120, null=True, blank=True)
#     dateto = models.CharField(max_length=120, null=True, blank=True)
#     shortdescription = models.CharField(max_length=120, null=True, blank=True)
#     # owner = models.ForeignKey(
#     #     Identity, on_delete=models.CASCADE, null=True, blank=True)
#     # resumee = models.ForeignKey(
#     #     Resumee, on_delete=models.CASCADE, null=True, blank=True)


# class Skill(CommonInfo):
#     # education
#     skillname = models.CharField(max_length=120, null=True, blank=True)
#     proficiency = models.CharField(max_length=120, null=True, blank=True)
#     # owner = models.ForeignKey(
#     #     Identity, on_delete=models.CASCADE, null=True, blank=True)
#     # resumee = models.ForeignKey(
#     #     Resumee, on_delete=models.CASCADE, null=True, blank=True)


# class Experience(CommonInfo):
#     # experience
#     companyname = models.CharField(max_length=120, null=True, blank=True)
#     position = models.CharField(max_length=120, null=True, blank=True)
#     datefrom = models.CharField(max_length=120, null=True, blank=True)
#     dateto = models.CharField(max_length=120, null=True, blank=True)
#     description = models.TextField(null=True, blank=True)
#     # owner = models.ForeignKey(
#     #     Identity, on_delete=models.CASCADE, null=True, blank=True)
#     # resumee = models.ForeignKey(
#     #     Resumee, on_delete=models.CASCADE, null=True, blank=True)
#     # end of experience
