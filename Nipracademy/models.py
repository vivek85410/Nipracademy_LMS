from django.db import models
from django.contrib.auth.models import User
import os
from django.template.defaultfilters import slugify
from django.urls import reverse



class Course(models.Model):
    name = models.CharField(max_length = 50 , null = False)
    slug = models.CharField(max_length = 50 , null = False ,unique=True)
    description = models.CharField(max_length = 200 , null = True )
    price = models.IntegerField(null=False)
    duration = models.PositiveIntegerField(help_text = "Duration in months")
    discount = models.IntegerField(null=False , default = 0) 
    active = models.BooleanField(default = False)
    thumbnail = models.ImageField(upload_to = "media/thumbnail_image") 
    date = models.DateTimeField(auto_now_add= True) 
    resource = models.FileField(upload_to = "media/resource", blank = True, null = True)
    length = models.IntegerField(null=False)
    

    def __str__(self):
        return self.name
    
class CourseProperty(models.Model):
    description  = models.CharField(max_length = 100 , null = False)
    course = models.ForeignKey(Course , null = False , on_delete=models.CASCADE)

    class Meta : 
        abstract = True


class Tag(CourseProperty):
    pass
    
class Prerequisite(CourseProperty):
    pass

class Learning(CourseProperty):
    pass


class Video(models.Model):
    title  = models.CharField(max_length = 100 , null = False)
    course = models.ForeignKey(Course , null = False , on_delete=models.CASCADE)
    serial_number = models.IntegerField(null=False)
    video_id = models.CharField(max_length = 100 , blank = True,null=True)
    video = models.FileField(upload_to="media/video_files",verbose_name="Video", blank=True, null=True)
    ppt = models.FileField(upload_to="media/ppt_files",verbose_name="Presentations", blank=True)
    Notes = models.FileField(upload_to="media/Notes_files",verbose_name="Notes", blank=True)
    is_preview = models.BooleanField(default = False)

    def __str__(self):
        return self.title
    
class UserCourse(models.Model):
    user = models.ForeignKey(User , null = False , on_delete=models.CASCADE)
    course = models.ForeignKey(Course , null = False , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.course.name}'
    
class Payment(models.Model):
    order_id = models.CharField(max_length = 100 , null = False)
    payment_id = models.CharField(max_length = 100)
    user_course = models.ForeignKey(UserCourse , null = True , blank = True ,  on_delete=models.CASCADE)
    user = models.ForeignKey(User ,  on_delete=models.CASCADE)
    course = models.ForeignKey(Course , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by{self.user.username} on {self.created_at}"

class contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()

class OfflineAddress(models.Model):
    branchname = models.CharField(max_length=122)
    address = models.CharField(max_length=500,null=False,blank=False)
    contact = models.IntegerField(null=True,blank=True)
   
    def __str__(self):
        return self.address
    
class Faculties(models.Model):
    name=models.CharField(max_length=100)
    qualifications=models.CharField(max_length=200)
    images=models.ImageField(upload_to="media/faculties_img",verbose_name="faculties",blank=True,null=True)

class Homepage_image(models.Model):
    pic=models.ImageField(upload_to="media/homepage_images",blank=True,null=True)
