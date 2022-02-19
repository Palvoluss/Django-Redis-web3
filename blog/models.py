from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone
from blog.utils import sendTransaction


class Category(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=200)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Post(models.Model): 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.ManyToManyField(Category)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def save(self):
        self.publishOnChain()
        super(Post, self).save()

    def publishOnChain(self):
        print('here')
        message=f'{self.author},{self.title},{self.description}, {self.text}, {self.created_date}, {self.published_date}'
        return sendTransaction(message)

