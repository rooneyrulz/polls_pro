from django.db import models

from question.models import Question

class Choice(models.Model):
    text = models.CharField(max_length=100, unique=True, blank=False, null=False)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    vote = models.IntegerField(blank=False, null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self, *args, **kwargs):
        return self.text
