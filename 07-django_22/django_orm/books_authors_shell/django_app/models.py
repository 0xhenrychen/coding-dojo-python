from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # def __repr__(self):
    #     return "Name: {}".format(self.name)
    
    # def __str__(self):
    #     return f"<Dojo object: {self.title} ({self.id})>"
    
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="authors")
    notes = models.CharField(default="These are the old notes.")
    notes = models.CharField(null=True)
    notes = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)