from django.db import models

from django.utils import timezone

# Create your models here.
class Snippet(models.Model):

    # created = models.DateTimeField(default=timezone.now())

    # modified = models.DateTimeField(default=timezone.now())
    
    title = models.CharField(max_length=256, blank=False, null=False, default="test")

    snippet = models.CharField(max_length=256, blank=False, null=False, default="test")

    language = models.CharField(max_length=256, blank=False, null=False, default="test")

    description = models.CharField(max_length=256, blank=True, null=True, default="test")

    def __str__(self):
        """ Sensible string representation of a snippet."""
        return "{0} | {1} | {2} | {3}".format(self.title, self.snippet, 
                self.language, self.description)

    def save(self, *args, **kwargs):
        """ Add created_at and updated_at timestamps. """
        # if not self.id:
        #     self.created = timezone.now()

        # self.modified = timezone.now()

        return super(Snippet, self).save(*args, **kwargs)

