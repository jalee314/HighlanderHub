from django.db import models

class Profile(models.Model):
  first_name = models.CharField(max_length=200, null=True)
  last_name = models.CharField(max_length=200, null=True)
  username = models.CharField(max_length=200, null=True)
  email = models.CharField(max_length=200, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)

  def __str__(self):
    return self.username

