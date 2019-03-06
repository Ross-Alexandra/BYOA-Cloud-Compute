from django.db import models


class Jobs(models.Model):
    finished = models.BooleanField(default=False)
    time_started = models.DateTimeField("date created")
    dockerfile = models.TextField()

    # Arbitrary max length for prototype.
    datastore_link = models.CharField(max_length=50)
