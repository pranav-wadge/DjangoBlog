from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField()
    image = models.ImageField(upload_to="blog/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title