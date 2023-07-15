from django.db import models

# Create your models here.
class CourseDetails(models.Model):
    c_name=models.CharField(max_length=50)
    c_des=models.TextField()
    c_image=models.ImageField(upload_to='courses', max_length=500)
    c_review=models.IntegerField(default=0)
    actual_price=models.IntegerField(default=0)
    discount_price=models.IntegerField(default=0)
    craeted=models.DateTimeField(auto_now=True, auto_now_add=False)
    
# class ApplicationData(models.Model):
    