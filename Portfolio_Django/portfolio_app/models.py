from django.db import models

# Create your models here.

class ContactMe(models.Model):
    email = models.EmailField()
    message = models.TextField(max_length=500)
    sent_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Email: {self.email} / Message: {self.message} / sent: {self.sent_time}"