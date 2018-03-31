from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length = 32)
    department = models.CharField(max_length = 32)
    description = models.CharField(max_length = 1024)
    date_and_time = models.CharField(max_length = 64)
    organiser = models.CharField(max_length = 32)
    contact_info = models.CharField(max_length = 32)

    def __str__(self):
        return self.event_name + ' - ' + self.description
