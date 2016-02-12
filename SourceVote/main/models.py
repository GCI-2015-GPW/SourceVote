from __future__ import unicode_literals

from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField()


class Project(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    contributors = models.IntegerField()
    url = models.URLField()
    technologies = models.ManyToManyField(Technology)

    def __unicode__(self):
        return self.title
