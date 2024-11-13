from django.db import models


class Question(models.Model):
	text = models.CharField(max_length=200)
	pub_date = models.DateTimeField("Date published")

	def __str__(self) -> str:
		return self.text


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self) -> str:
		return f'{self.text} ({self.votes})'