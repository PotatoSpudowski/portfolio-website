from django.db import models

class Signup(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

