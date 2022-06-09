from django.db import models


# Create your models here.
class Educator(models.Model):
    edu_name = models.CharField(max_length=20)
    edu_major = models.CharField(max_length=20) 
    edu_exp = models.CharField(max_length=20)
    edu_course_1 = models.CharField(max_length=20)
    edu_course_2 = models.CharField(max_length=20)

    #Converting an Object into String (Bydefault ORM returns obejct only)
    def __str__(self):
        return self.edu_name
