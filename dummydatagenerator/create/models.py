from django.db import models

# Create your models here.
class Post(models.Model):
    column_name = models.CharField(max_length=50)
    # column_type = models.CharField(max_length=50)
    # document = models.FileField(upload_to='uploads/%Y/%m/%d/', validators=[FileExtensionValidator(['json',])])
    # uploaded_at = models.DateTimeField(auto_now_add=True)