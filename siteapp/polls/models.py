from django.db import models

class PollResult(models.Model):
    name = models.CharField(max_length=100)
    choice = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.choice}"
