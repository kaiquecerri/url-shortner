from django.db import models
from django.contrib.auth.models import User

class Url(models.Model):
    name = models.CharField(max_length=30)
    original_url = models.CharField(max_length=2048)
    shortned_url = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'urls'

