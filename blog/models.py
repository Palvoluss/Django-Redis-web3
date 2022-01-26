from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=200)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.ManyToManyField(Category)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


