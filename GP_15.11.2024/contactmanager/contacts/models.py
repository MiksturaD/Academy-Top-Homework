from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField
    phone = models.CharField(max_length=100, verbose_name="Phone")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    def __str__(self):
        return f"{self.name} {self.email} {self.phone} {self.created_at}"


