from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=120, unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self, *args, **kwargs):
        return self.text
