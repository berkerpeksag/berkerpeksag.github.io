from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    LANGUAGES = (
        (u'tr', u'Turkish'),
        (u'en', u'English'),
    )

    author = models.ForeignKey(User)
    status = models.BooleanField('Active', default=False)
    archive = models.BooleanField(default=False)
    language = models.CharField(max_length=2, choices=LANGUAGES, default='tr')
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

    def get_absolute_url(self):
        return '/{:s}/'.format(self.slug)

    def __unicode__(self):
        return self.title
