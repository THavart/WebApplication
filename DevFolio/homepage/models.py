from django.db import models

class Snippet(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=75)
    subject = models.CharField(max_length=100)
    content = models.TextField()
    def __str__(self):
        return self.name
2
