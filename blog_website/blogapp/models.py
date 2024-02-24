from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title=models.CharField(max_length= 200, verbose_name="blog title",unique=True)
    description=models.TextField()
    content=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    thumbnail=models.ImageField(upload_to="thumbnails", default="default.jpg")

    def __str__(self) -> str:
        return f'{self.title}'