from django.db import models

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length = 32)
    event_url = models.SlugField(max_length = 32)
    description = models.TextField(max_length = 1024)
    #
    date = models.DateTimeField()
    organiser = models.CharField(max_length = 32)
    contact_info = models.EmailField(max_length = 32)
    image = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.event_name
    def snippet(self):
        return self.description[:100] + '.....'
