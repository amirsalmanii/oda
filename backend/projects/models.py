from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="projects/")
    body = models.TextField()

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.title