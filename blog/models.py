import json
from django.db import models
from django.conf import settings
from django.db import models
from django.http import JsonResponse
from django.utils import timezone
from django.contrib import admin

from blog.utils import sendTransactionAndGetTxId


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
    transaction_id = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(Category)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def save(self):
        self.transaction_id = self.publishOnChainAsJson()
        super(Post, self).save()

    def publishOnChainAsJson(self):
        if self == None:
            return None
        jsonObj = {}
        jsonObj["Author"] = str(self.author)
        jsonObj["title"] = self.title
        jsonObj["description"] = self.description
        jsonObj["text"] = self.text
        jsonObj["created_date"] = str(self.created_date)
        jsonObj["published_date"] = str(self.published_date)
        return sendTransactionAndGetTxId(json.dumps(jsonObj))

class PostAdmin(admin.ModelAdmin):
    model = Post
    exclude = ['transaction_id']