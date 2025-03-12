from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Modification(models.Model):
    file = models.ForeignKey(File, related_name='modifications', on_delete=models.CASCADE)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modification_date = models.DateTimeField(auto_now_add=True)
    change_description = models.TextField()
    
    def __str__(self):
        return f"Modified by {self.modified_by.username} on {self.modification_date}"
