from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='posts/', blank=True, null=True)

    def __str__(self):
        return self.title