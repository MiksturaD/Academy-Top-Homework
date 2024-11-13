from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="First Name")
    last_name = models.CharField(max_length=30, verbose_name="Last Name")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class TopBooks(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='top_books')
    title = models.CharField(max_length=200,verbose_name="Title")
    pub_date = models.DateField(verbose_name='Date published')
    votes = models.IntegerField(default=0,verbose_name="Votes")

    def __str__(self):
        return self.title