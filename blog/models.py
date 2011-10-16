from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
import markdown


class Post(models.Model):
    author = models.ForeignKey(User)
    status = models.BooleanField(default=False)
    enable_comments = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now())
    update_date = models.DateTimeField(default=datetime.now())

    class Meta:
        ordering = ['-pub_date']
        
    @property
    def is_active(self):
        return self.status

    def __unicode__(self):
        return self.title