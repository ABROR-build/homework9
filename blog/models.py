from django.db import models
from accounts.models import Accounts


class Blogs(models.Model):
    author = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=1000)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    class Meta:
        db_table = 'Blogs'

    def __str__(self):
        return self.title
