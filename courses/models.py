from django.db import models
from users.models import User

# Course model
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    trainer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
# Unit model
class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title
# Assessment model
class Assessment(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='assessments')
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title