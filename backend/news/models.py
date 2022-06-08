from django.db import models
from accounts.models import User


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news')
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="news", null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        return self.title
