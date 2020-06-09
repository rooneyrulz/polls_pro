from django.db import models

class Language(models.Model):
    name        = models.CharField(max_length=120, unique=True, blank=False, null=False)
    created_at  = models.DateTimeField(auto_now_add=True)

    @property
    def frameworks(self, *args, **kwargs):
        return self.framework.all()
        
    def __str__(self, *args, **kwargs):
        return self.name