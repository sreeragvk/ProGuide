from django.db import models

class category(models.Model):
    course_category=models.CharField(max_length=200)
    c_description=models.TextField()
    image=models.ImageField(upload_to='courses/category',null=True,blank=True)
    
    def __str__(self):
        return self.course_category 

class course(models.Model):
    course_name=models.CharField(max_length=200)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    description=models.TextField()
    tutor=models.CharField(max_length=200)
    image=models.ImageField(upload_to='courses/course',null=True,blank=True)
    video_file=models.FileField( upload_to='courses/course')
    duration=models.DecimalField(max_digits=2, decimal_places=1)
    students=models.IntegerField()
    rating=models.DecimalField(max_digits=2, decimal_places=1)
    
    def __str__(self):
        return self.course_name
        
    
    
    
