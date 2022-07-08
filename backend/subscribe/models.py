from django.db import models


class Subscribe(models.Model):
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
