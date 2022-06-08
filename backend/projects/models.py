from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="projects/", null=True, blank=True)
    body = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.title