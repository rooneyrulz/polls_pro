from django.db import models
from language.models import Language

class Framework(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    language = models.ForeignKey(Language, related_name='framework', on_delete=models.CASCADE)
    vote = models.IntegerField(blank=False, null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self, *args, **kwargs):
        return self.name
