from django.db import models
from django.contrib.auth.models import User

class Language(models.Model):
    name        = models.CharField(max_length=120, unique=True, blank=False, null=False)
    owner       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='language', null=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    @property
    def frameworks(self, *args, **kwargs):
        return self.framework.all()
        
    def __str__(self, *args, **kwargs):
        return self.name